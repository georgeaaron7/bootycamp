# Transformer Architecture — Theory (Day 11)

## 1. Why Transformers?
Traditional RNNs and LSTMs process sequences **sequentially**, limiting parallelism and requiring long dependency paths.  
Transformers process all tokens **in parallel** using **self-attention**, allowing:
- better long-range dependency learning  
- higher training speed  
- scalability to very large models  

---

## 🎥 Recommended Videos & Playlists

### 🔹 Transformer Architecture Theory (Engish)
https://youtu.be/ZhAz268Hdpw?si=douUqG1Dp2O4lWDL

### 🔹 Complete Transformer Architecture Playlist (Hindi)
https://youtube.com/playlist?list=PLkBMe2eZMRQ2VKEtoL0GVUrNzEiXfgj07&si=G8vOYUUunpA9msbd

### 🔹 Complete Transformer Architecture Playlist (English)
https://youtube.com/playlist?list=PLuhqtP7jdD8CQTxwVsuiFYGvHtFpNhlR3&si=qUnNpionceu2Am5x

---

## 2. Scaled Dot-Product Attention
Attention computes relationships between tokens via Queries (Q), Keys (K), and Values (V).

### Formula:
```
Attention(Q, K, V) = softmax( (QKᵀ) / √d_k ) V
```

### Intuition:
- Q compares with K to find similarity  
- softmax gives weights  
- weights multiply V to produce contextual representation  

---

## 3. Multi-Head Attention (MHA)
Instead of using a single attention head, Transformers use **multiple heads**.

### Why?
- Each head captures different relationships  
- Some heads may detect syntax, others semantic meaning  

### Process:
1. Split embeddings into `num_heads`  
2. Apply attention in parallel  
3. Concatenate heads  
4. Linear projection back to `d_model`  

---

## 4. Positional Encoding
Transformers have no inherent awareness of token **order**.  
Sinusoidal positional encodings inject sequence information.

### Formulas:
```
PE(pos, 2i)   = sin(pos / 10000^(2i/d_model))
PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))
```

### Properties:
- Continuous and smooth  
- Relative positions easily captured  
- No learning required  

---

## 5. Feed Forward Network (FFN)
Each token independently passes through a **2-layer MLP**:

```
FFN(x) = ReLU(xW1 + b1)W2 + b2
```

This adds more transformation capacity.

---

## 6. LayerNorm + Residual Connections
Transformers heavily use:

### Residual:
```
x + Sublayer(x)
```

### LayerNorm:
Improves stability by normalizing across feature dimensions.

---

## 7. Encoder Block Architecture
```
Input
 → Multi-Head Self Attention
    → Add & LayerNorm
 → Feed Forward Network
    → Add & LayerNorm
Output
```

---

## 8. Masking
Used to:
- ignore padded tokens  
- prevent attending to future positions (in decoders)  

Masking ensures attention weights zero-out invalid positions.

---

## Summary
A Transformer Encoder Block uses:
- Self-Attention  
- Multi-Head projections  
- Positional Encoding  
- Feed Forward Networks  
- Layer Normalization  
- Residual Connections  

These components together enable powerful sequence understanding and form the backbone of all modern LLMs.
