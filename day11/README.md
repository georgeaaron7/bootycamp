# DAY 11 — TRANSFORMER ARCHITECTURE
### Understanding Attention, Multi-Head Attention, Positional Encoding & Encoder Blocks

---

## 🚀 Overview
Day 11 introduces the **Transformer Architecture**, the foundation of modern LLMs such as GPT, LLaMA, Gemini and Claude.  
You will understand how transformers replace RNNs using **self-attention**, enabling parallelism and long-range context learning.

---

## 🎯 Learning Goals
- Understand the math behind self-attention  
- Learn Queries, Keys, Values  
- Implement scaled dot-product attention  
- Implement multi-head attention  
- Add sinusoidal positional encoding  
- Build a transformer encoder block in PyTorch  
- Run a full forward pass & inspect shapes  

---

## 📂 Folder Structure
```
day11
│
├── README.md
├── theory.md
├── tutorial.md
├── requirements.txt
├── .gitignore
│
└── code/
    ├── model_components.py
    ├── utils.py
    ├── example_inputs.py
    └── demo.py
```

---

## 🔥 Hands-On Tasks
- Build Scaled Dot-Product Attention  
- Build Multi-Head Attention  
- Implement Positional Encoding  
- Build Transformer Encoder Block  
- Run `demo.py` to test a forward pass  

---

## ▶️ How to Run
```bash
cd day11-transformer
pip install -r requirements.txt
python code/demo.py
```

---

## 📚 Resources
- The Illustrated Transformer — Jay Alammar  
- Attention Is All You Need — Paper  
- PyTorch Transformer Docs  
- 3Blue1Brown — Attention Mechanism  

---