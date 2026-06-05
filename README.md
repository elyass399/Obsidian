# Stateful GraphRAG — LLM Wiki

A knowledge graph that grows from your documents. Load a PDF, watch the graph expand.

Inspired by Andrej Karpathy's LLM-Wiki pattern.

---

## What it does

Most RAG systems treat knowledge as a flat pile of text chunks. This system builds a **persistent knowledge graph** — every document you load adds to it, merging with existing knowledge instead of rebuilding from scratch.

**Pipeline:**
```
PDF → Markdown → Entity Extraction → Entity Resolution → FalkorDB → Obsidian Wiki
```

---

## How it works

1. **PDF → Markdown** — extracts clean text from any PDF
2. **Entity Extraction** — Mistral LLM reads the text and returns entities + relations as JSON
3. **Entity Resolution** — hybrid approach: sentence embeddings filter candidates by cosine similarity, then Mistral decides if two entities are the same thing and logs every decision
4. **FalkorDB** — stores the knowledge graph with Cypher MERGE (no duplicates)
5. **Obsidian Sync** — generates one `.md` file per node with `[[wikilinks]]` — Obsidian renders it as a live interactive graph

---

## Stack

| Component | Technology |
|---|---|
| Graph DB | FalkorDB |
| LLM | Mistral (free tier) |
| Embeddings | Sentence Transformers |
| Backend | FastAPI |
| Frontend | Vanilla HTML + D3.js |
| Wiki | Obsidian |

---



## Project Structure

```
wiki/
├── api.py                  ← FastAPI backend
├── extract_entities.py     ← PDF → entities → FalkorDB
├── entity_resolution.py    ← hybrid deduplication
├── watcher.py              ← FalkorDB → Obsidian .md files
├── pdf_to_md.py            ← PDF → Markdown
├── frontend/
│   ├── index.html          ← upload + chat UI
│   └── graph.html          ← D3.js graph visualizer
└── log.md                  ← every LLM decision logged here
```

---

