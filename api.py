from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from falkordb import FalkorDB
from pathlib import Path
from dotenv import load_dotenv
from mistralai import Mistral
import os

load_dotenv()
client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    question: str

@app.get("/status")
async def get_status():
    try:
        db = FalkorDB(host='localhost', port=6379)
        g = db.select_graph('wiki')
        result = g.query("MATCH (n:Entity) RETURN count(n)")
        node_count = result.result_set[0][0]
        md_count = len(list(Path("./manuals").glob("*.md")))
        return {
            "status": "ok",
            "node_count": node_count,
            "md_files": md_count
        }
    except Exception as e:
        return {"status": "error", "detail": str(e)}

@app.get("/graph")
async def get_graph():
    db = FalkorDB(host='localhost', port=6379)
    g = db.select_graph('wiki')
    nodes_result = g.query("MATCH (n:Entity) RETURN n.name, n.type")
    edges_result = g.query("MATCH (a)-[r]->(b) RETURN a.name, type(r), b.name")
    nodes = [{"name": r[0], "type": r[1]} for r in nodes_result.result_set]
    edges = [{"from": r[0], "relation": r[1], "to": r[2]} for r in edges_result.result_set]
    return {"nodes": nodes, "edges": edges}

@app.post("/upload")
async def upload_pdf(file: UploadFile):
    pdf_path = Path("./dati") / file.filename
    with open(pdf_path, "wb") as f:
        f.write(await file.read())

    from pdf_to_md import convert_pdf, post_process
    md = convert_pdf(pdf_path)
    md = post_process(md)
    out_path = Path("./manuals") / (pdf_path.stem + ".md")
    out_path.write_text(md, encoding="utf-8")

    from extract_entities import extract_entities, push_to_falkor
    text = out_path.read_text(encoding="utf-8")
    result = extract_entities(text)
    push_to_falkor(result)

    from watcher import run as watcher_run
    watcher_run()

    return {"status": "ok", "filename": file.filename}

@app.post("/query")
async def post_query(req: QueryRequest):
    question = req.question

    db = FalkorDB(host='localhost', port=6379)
    g = db.select_graph('wiki')

    schema_result = g.query("MATCH ()-[r]->() RETURN distinct type(r) LIMIT 20")
    relations = [r[0] for r in schema_result.result_set]

    cypher_prompt = f"""Sei un esperto di FalkorDB e Cypher.
Converti questa domanda in una query Cypher per un graph di Machine Learning.
I nodi hanno label :Entity con proprietà name e type.
Le relazioni esistenti nel graph sono: {relations}
Rispondi SOLO con la query Cypher, niente altro.

Domanda: {question}"""

    cypher_response = client.chat.complete(
        model="mistral-small-latest",
        messages=[{"role": "user", "content": cypher_prompt}]
    )
    cypher = cypher_response.choices[0].message.content.strip()
    cypher = cypher.replace("```cypher", "").replace("```", "").strip()

    try:
        result = g.query(cypher)
        graph_context = str(result.result_set[:20])
    except Exception as e:
        graph_context = f"Query fallita: {e}"

    answer_prompt = f"""Usa questi dati dal knowledge graph per rispondere alla domanda.

Domanda: {question}
Dati dal graph: {graph_context}

Rispondi in modo chiaro e conciso."""

    answer_response = client.chat.complete(
        model="mistral-small-latest",
        messages=[{"role": "user", "content": answer_prompt}]
    )

    return {
        "question": question,
        "cypher": cypher,
        "answer": answer_response.choices[0].message.content.strip()
    }