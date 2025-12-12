import torch
from model_components import TransformerEncoderBlock
from utils import PositionalEncoding
from example_inputs import random_input


def main():
    torch.manual_seed(0)

    batch = 2
    seq_len = 12
    d_model = 64

    x, mask = random_input(batch=batch, seq_len=seq_len, d_model=d_model, pad=True)

    pos_enc = PositionalEncoding(d_model)
    x = pos_enc(x)

    encoder = TransformerEncoderBlock(
        d_model=d_model,
        num_heads=4,
        d_ff=256,
        dropout=0.1,
    )

    out, attn_weights = encoder(x, mask)

    print("Input shape       :", x.shape)
    print("Output shape      :", out.shape)
    print("Attention weights :", attn_weights.shape)
    print("Forward pass successful!")


if __name__ == "__main__":
    main()
