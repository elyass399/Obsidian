from dotenv import load_dotenv
from mistralai import Mistral
from falkordb import FalkorDB
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import os, json

load_dotenv()
client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
model = SentenceTransformer('all-mpnet-base-v2')

THRESHOLD = 0.7

def get_existing_nodes():
    db = FalkorDB(host='localhost', port=6379)
    g = db.select_graph('wiki')
    result = g.query("MATCH (n:Entity) RETURN n.name, n.type")
    return [{"name": row[0], "type": row[1]} for row in result.result_set]

def find_candidates(new_entity: str, existing_nodes: list) -> list:
    if not existing_nodes:
        return []
    new_vec = model.encode([new_entity])
    existing_vecs = model.encode([n["name"] for n in existing_nodes])
    scores = cosine_similarity(new_vec, existing_vecs)[0]
    candidates = []
    for i, score in enumerate(scores):
        if score > THRESHOLD:
            candidates.append({"node": existing_nodes[i], "score": float(score)})
    return sorted(candidates, key=lambda x: x["score"], reverse=True)

def mistral_decide(new_entity: str, candidate: str) -> dict:
    prompt = f"""Sei un esperto di Machine Learning.
Queste due entità sono la stessa cosa?
- Entità 1: "{new_entity}"
- Entità 2: "{candidate}"

Rispondi SOLO in JSON:
{{"same": true/false, "reason": "spiegazione breve"}}"""
    
    response = client.chat.complete(
        model="mistral-small-latest",
        messages=[{"role": "user", "content": prompt}]
    )
    raw = response.choices[0].message.content.strip()
    raw = raw.replace("```json", "").replace("```", "").strip()
    return json.loads(raw)

def resolve_entity(new_entity: str, new_type: str) -> str:
    existing = get_existing_nodes()
    candidates = find_candidates(new_entity, existing)
    
    if not candidates:
        print(f"  NUOVO: '{new_entity}'")
        return new_entity
    
    for c in candidates[:3]:  # top 3 candidati
        decision = mistral_decide(new_entity, c["node"]["name"])
        log_decision(new_entity, c["node"]["name"], c["score"], decision)
        
        if decision["same"]:
            print(f"  MERGE: '{new_entity}' → '{c['node']['name']}' ({decision['reason']})")
            return c["node"]["name"]
    
    print(f"  NUOVO: '{new_entity}'")
    return new_entity

def log_decision(new: str, existing: str, score: float, decision: dict):
    with open("log.md", "a", encoding="utf-8") as f:
        status = "MERGE" if decision["same"] else "NUOVO"
        f.write(f"- [{status}] '{new}' vs '{existing}' (score: {score:.2f}) → {decision['reason']}\n")

# Test
if __name__ == "__main__":
    test_cases = ["neurons", "ANN", "Deep Learning", "fotosintesi"]
    for entity in test_cases:
        result = resolve_entity(entity, "concetto")
        print(f"  Risultato finale: '{result}'\n")