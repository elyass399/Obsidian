from dotenv import load_dotenv
from mistralai import Mistral
from pathlib import Path
import os, json, re, unicodedata
from falkordb import FalkorDB
from entity_resolution import resolve_entity

load_dotenv()
client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))

PROMPT_TEMPLATE = """Leggi questo testo di Machine Learning / Computer Vision.
Estrai SOLO concetti presenti nel testo, non inventare.
Ogni relazione deve essere tra due entità già estratte.
Esempi di relazione: esempio_di, sinonimo, correlato_a, dipende_da, allenato_con.
Se nessuna si adatta, genera una più precisa.

Rispondi SOLO in JSON, niente altro:
{{
  "entities": [
    {{"name": "nome", "type": "concetto|algoritmo|dataset|metrica|persona|other"}}
  ],
  "relations": [
    {{"from": "entità1", "relation": "verbo/azione", "to": "entità2"}}
  ]
}}

TESTO:
{testo}"""

def sanitize_relation(rel: str) -> str:
    rel = unicodedata.normalize("NFD", rel)
    rel = "".join(c for c in rel if unicodedata.category(c) != "Mn")
    rel = re.sub(r"[^a-zA-Z0-9_]", "_", rel)
    return rel.upper()

def extract_entities(text: str) -> dict:
    prompt = PROMPT_TEMPLATE.format(testo=text[:2000])
    response = client.chat.complete(
        model="mistral-small-latest",
        messages=[{"role": "user", "content": prompt}]
    )
    raw = response.choices[0].message.content.strip()
    raw = raw.replace("```json", "").replace("```", "").strip()
    return json.loads(raw)

def push_to_falkor(data: dict):
    db = FalkorDB(host='localhost', port=6379)
    g = db.select_graph('wiki')

    for entity in data["entities"]:
        type_ = entity["type"]
        name = resolve_entity(entity["name"], type_)
        name = name.replace("'", "\\'")
        g.query(f"MERGE (n:Entity {{name: '{name}', type: '{type_}'}})")

    for rel in data["relations"]:
        from_ = rel["from"].replace("'", "\\'")
        to_ = rel["to"].replace("'", "\\'")
        relation = sanitize_relation(rel["relation"])
        g.query(f"""
            MATCH (a:Entity {{name: '{from_}'}})
            MATCH (b:Entity {{name: '{to_}'}})
            MERGE (a)-[:{relation}]->(b)
        """)

    print(f"Caricati: {len(data['entities'])} nodi, {len(data['relations'])} relazioni")

# Main
if __name__ == "__main__":
    md_files = sorted(Path("./manuals").glob("*.md"))
    for md_file in md_files:
        text = md_file.read_text(encoding="utf-8")
        print(f"\nProcessing: {md_file.name}")
        result = extract_entities(text)
        push_to_falkor(result)
    print("\nDone — tutti i file processati.")