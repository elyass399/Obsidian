from falkordb import FalkorDB
from pathlib import Path
import re

OUTPUT_DIR = Path("./obsidian")

def get_all_nodes():
    db = FalkorDB(host='localhost', port=6379)
    g = db.select_graph('wiki')
    result = g.query("MATCH (n:Entity) RETURN n.name, n.type")
    return [{"name": r[0], "type": r[1]} for r in result.result_set]

def get_node_relations(node_name):
    db = FalkorDB(host='localhost', port=6379)
    g = db.select_graph('wiki')
    safe = node_name.replace("'", "\\'")
    out = g.query(f"MATCH (n:Entity {{name: '{safe}'}})-[r]->(m) RETURN type(r), m.name")
    inc = g.query(f"MATCH (a)-[r]->(n:Entity {{name: '{safe}'}}) RETURN type(r), a.name")
    return {
        "out": [{"rel": r[0], "name": r[1]} for r in out.result_set],
        "in":  [{"rel": r[0], "name": r[1]} for r in inc.result_set]
    }

def safe_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "_", name)

def generate_md(node):
    relations = get_node_relations(node["name"])
    md = f"# {node['name']}\n**tipo:** {node['type']}\n\n"
    if relations["out"]:
        md += "## Relazioni in uscita\n"
        for r in relations["out"]:
            md += f"- {r['rel']} → [[{r['name']}]]\n"
    if relations["in"]:
        md += "\n## Relazioni in entrata\n"
        for r in relations["in"]:
            md += f"- [[{r['name']}]] → {r['rel']}\n"
    return md

def run():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    nodes = get_all_nodes()
    print(f"Generando {len(nodes)} file .md...")
    for node in nodes:
        md = generate_md(node)
        fname = safe_filename(node["name"])
        (OUTPUT_DIR / f"{fname}.md").write_text(md, encoding="utf-8")
    print("Done — apri cartella obsidian/ in Obsidian!")

if __name__ == "__main__":
    run()