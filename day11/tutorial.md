# Day 11 — Hands-On Tutorial

## 🎯 Objective
Implement the core components of a Transformer Encoder Block and run a full forward pass to deeply understand how self-attention works in practice.

---

## 🧠 Step-by-Step Tasks

### 1️⃣ Implement Scaled Dot-Product Attention  
File to edit: `code/model_components.py`

Key goals:
- Compute QKᵀ  
- Scale by √dₖ  
- Apply softmax  
- Multiply with V  
- Understand attention weights  

---

### 2️⃣ Implement Multi-Head Attention  
Key concepts:
- Split embedding dimension into `num_heads`  
- Reshape tensors correctly  
- Parallel attention across heads  
- Concatenate and project output  

---

### 3️⃣ Implement Positional Encoding  
File: `code/utils.py`

Why?
Transformers do not understand order — positional encodings add sequence information.

You will:
- Implement sinusoidal encodings  
- Add them to token embeddings  

---

### 4️⃣ Build Transformer Encoder Block  
Components:
- Multi-Head Attention  
- Add & LayerNorm  
- Feed Forward Network  
- Add & LayerNorm  

This is the core transformer layer used in LLMs.

---

### 5️⃣ Run Demo  
File: `code/demo.py`

The demo performs:
- Random input generation  
- Positional encoding  
- Forward pass through encoder  
- Prints shapes:  
  - input  
  - output  
  - attention weights  

This confirms your implementation is correct.

---

## 📝 Recommended Experiments
Try the following to deepen understanding:

- Change number of heads (e.g., 2 → 4 → 8)  
- Change sequence length (8 → 16 → 32)  
- Visualize attention weights  
- Add multiple encoder layers  
- Try different feed-forward dimensions (`d_ff = 128, 256, 512`)  

---

## 📌 Learning Outcomes
By completing this tutorial, you will:
- Understand the math behind attention  
- Know how multi-head attention is implemented  
- Understand positional encodings in detail  
- Build and run a Transformer Encoder Block  
- Gain confidence to explore decoder blocks, BERT, GPT, etc.  

---

## 🚀 Next Steps
After Day 11, you can:
- Implement a small Transformer encoder classifier  
- Implement a GPT-style decoder block  
- Learn about RNN vs Transformer performance differences  

