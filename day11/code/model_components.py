import torch
import torch.nn as nn
import math
from typing import Optional


class ScaledDotProductAttention(nn.Module):
    def __init__(self, d_k: int, dropout: float = 0.0):
        super().__init__()
        self.scale = math.sqrt(d_k)
        self.dropout = nn.Dropout(dropout) if dropout > 0 else None

    def forward(self, Q, K, V, mask: Optional[torch.Tensor] = None):
        # Q, K, V: (batch, heads, seq_len, head_dim)
        scores = torch.matmul(Q, K.transpose(-2, -1)) / self.scale

        if mask is not None:
            scores = scores.masked_fill(mask, float("-inf"))

        attention_weights = torch.softmax(scores, dim=-1)

        if self.dropout is not None:
            attention_weights = self.dropout(attention_weights)

        output = torch.matmul(attention_weights, V)
        return output, attention_weights


class MultiHeadAttention(nn.Module):
    def __init__(self, d_model: int, num_heads: int, dropout: float = 0.0):
        super().__init__()

        assert d_model % num_heads == 0, "d_model must be divisible by num_heads"

        self.d_model = d_model
        self.num_heads = num_heads
        self.head_dim = d_model // num_heads

        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)

        self.out_proj = nn.Linear(d_model, d_model)
        self.attention = ScaledDotProductAttention(self.head_dim, dropout)

    def forward(self, x, mask: Optional[torch.Tensor] = None):
        batch_size, seq_len, _ = x.size()

        Q = self.W_q(x)
        K = self.W_k(x)
        V = self.W_v(x)

        # reshape to (batch, heads, seq_len, head_dim)
        Q = Q.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        K = K.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        V = V.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)

        if mask is not None:
            mask = mask.unsqueeze(1).unsqueeze(1)  # (batch, 1, 1, seq_len)

        attn_out, attn_weights = self.attention(Q, K, V, mask)

        # merge heads back
        attn_out = attn_out.transpose(1, 2).contiguous().view(batch_size, seq_len, self.d_model)

        output = self.out_proj(attn_out)
        return output, attn_weights


class PositionwiseFeedForward(nn.Module):
    def __init__(self, d_model: int, d_ff: int, dropout: float = 0.0):
        super().__init__()
        self.ffn = nn.Sequential(
            nn.Linear(d_model, d_ff),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(d_ff, d_model)
        )

    def forward(self, x):
        return self.ffn(x)


class TransformerEncoderBlock(nn.Module):
    def __init__(self, d_model=512, num_heads=8, d_ff=2048, dropout=0.1):
        super().__init__()
        self.mha = MultiHeadAttention(d_model, num_heads, dropout)
        self.norm1 = nn.LayerNorm(d_model)

        self.ffn = PositionwiseFeedForward(d_model, d_ff, dropout)
        self.norm2 = nn.LayerNorm(d_model)

        self.dropout = nn.Dropout(dropout)

    def forward(self, x, mask=None):
        attn_out, attn_weights = self.mha(x, mask)
        x = self.norm1(x + self.dropout(attn_out))

        ffn_out = self.ffn(x)
        x = self.norm2(x + self.dropout(ffn_out))

        return x, attn_weights
