# Day 13 — RAG Hands-On Tutorial

## 🎯 Objective
Build a working Retrieval-Augmented Generation (RAG) system that:
1. Ingests documents  
2. Chunks & embeds them  
3. Stores embeddings in a vector database  
4. Retrieves relevant chunks  
5. Uses an LLM to answer queries using retrieved knowledge  

---

## 🧠 Step-by-Step Tasks

### 1️⃣ Implement Text Chunking
File: `embed_store.py`

Goals:
- Split large text into small, meaningful chunks  
- Typical chunk size: **250–400 words**  
- Avoid cutting mid-sentence if possible  

---

### 2️⃣ Implement Embedding + Storage (ChromaDB)
File: `embed_store.py`

Steps:
1. Convert each chunk into embeddings  
2. Store them in a Chroma collection  
3. Maintain mapping of `id → chunk`  

---

### 3️⃣ Implement Query Retrieval
File: `query_engine.py`

Flow:
- Embed user query  
- Perform vector similarity search  
- Retrieve top-k similar chunks  

---

### 4️⃣ Implement RAG Answer Generation
File: `query_engine.py`

Process:
1. Construct prompt:
```
Context:
<retrieved_chunks>

Question:
<user_query>

Answer:
```
2. Feed to an LLM (GPT2, LLaMA, any HF model)  
3. Generate a grounded response  

---

### 5️⃣ Run Demo
File: `demo.py`

The demo:
- Loads sample text  
- Ingests into ChromaDB  
- Performs retrieval  
- Generates the RAG answer  

Run it:
```bash
python code/demo.py
```

---

## 📝 Experiments
Try:
- Different chunk sizes (100, 200, 400)  
- Different embedding models  
- Changing `top_k` values  
- Using a better LLM (LLaMA, Mistral)  

---

## 📌 Learning Outcomes
By completing this tutorial, you will understand:
- How RAG retrieves relevant data  
- How embeddings & vector search work in practice  
- How to build RAG systems with ChromaDB  
- How LLMs generate answers using external knowledge  

---

## 🚀 Next Steps
After Day 13, you can:
- Build a PDF Q&A bot  
- Connect RAG with Streamlit UI  
- Add multi-document ingestion  
- Visualize embeddings using PCA or t-SNE  
