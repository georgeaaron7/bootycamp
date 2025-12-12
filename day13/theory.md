# Retrieval-Augmented Generation (RAG) — Theory (Day 13)

## 1. Why RAG?
LLMs often hallucinate because:
- They rely only on pretraining data
- They cannot access updated external knowledge
- They may guess when context is missing

RAG solves this by retrieving **real external information** during inference.

---

## 🎥 Recommended Videos (In-depth RAG Explanation)

### 🔹 RAG — English Tutorial  
https://youtu.be/sVcwVQRHIc8?si=WzdoBnHRHtA4C_g6

### 🔹 RAG — Hindi Tutorial  
https://youtu.be/J5_-l7WIO_w?si=kGQ-H2nKp3H4I6zv

---

## 2. RAG Architecture
```
User Query
      ↓
Embed Query
      ↓
Vector DB Similarity Search (Top-k)
      ↓
LLM receives: Query + Retrieved Context
      ↓
Final Answer
```

---

## 3. Embeddings
Embeddings convert text into dense vector representations.

- Semantic similarity → close vectors  
- Different meanings → distant vectors  

Popular embedding models:
- all-MiniLM-L6-v2
- BGE-small
- text-embedding-3-small

---

## 4. Vector Databases
A vector DB stores embeddings & supports fast similarity search.

Options:
- ChromaDB
- FAISS
- Pinecone
- Weaviate

Core operations:
- add(documents, embeddings)
- query(query_embedding, top_k)

---

## 5. Chunking
Documents are split into smaller pieces (200–500 tokens).

Why chunk?
- Improves retrieval accuracy  
- Helps model focus on relevant info  
- Prevents irrelevant long blocks  

---

## 6. RAG Pipeline

### Ingestion Phase
1. Load a document
2. Chunk it
3. Embed each chunk
4. Store embeddings into vector DB

### Query Phase
1. Embed user query
2. Retrieve relevant chunks
3. Pass (query + retrieved context) to LLM
4. Generate final grounded answer

---

## 7. Why RAG Works
- Reduces hallucinations  
- Injects external knowledge into LLMs  
- No need to retrain models  
- Updated knowledge can be added anytime  

---

## 8. Use Cases
- Chatbots with specific domain documents  
- PDF question-answering  
- Enterprise knowledge bots  
- Legal, medical, and educational assistants  

---

## Summary
RAG strengthens LLMs by combining:
- Retrieval (search)
- Generation (LLM reasoning)

This creates powerful, factual, and grounded AI systems.
