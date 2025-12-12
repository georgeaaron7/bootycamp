# DAY 13 — Retrieval-Augmented Generation (RAG)
### Adding External Knowledge to LLMs using Embeddings + Vector Databases

---

## 🚀 Overview
Retrieval-Augmented Generation (RAG) enhances LLMs by combining:
- **document retrieval** using vector similarity search  
- **LLM reasoning** using retrieved context  

RAG reduces hallucinations and enables models to use **external, updated, domain-specific knowledge**.

---

## 🎯 Learning Goals
- Understand embeddings & vector search  
- Learn how vector databases store & retrieve knowledge  
- Implement chunking strategies  
- Build a full RAG pipeline (ingest → retrieve → generate)  
- Use ChromaDB + SentenceTransformers  
- Query the RAG system to answer questions using documents  

---

## 📂 Folder Structure
```
day13-rag/
│
├── README.md
├── theory.md
├── tutorial.md
├── requirements.txt
├── .gitignore
│
└── code/
    ├── rag_pipeline.py
    ├── embed_store.py
    ├── query_engine.py
    └── demo.py
```

---

## ▶️ How to Run
```bash
cd day13-rag
pip install -r requirements.txt

python code/demo.py
```

---

## 📚 Recommended Resources
- AssemblyAI — RAG Explained  
- ChromaDB Docs  
- LangChain RAG Docs  
- SentenceTransformers Docs  

---
