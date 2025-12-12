import torch


def random_input(batch=2, seq_len=10, d_model=64, pad=True):
    x = torch.randn(batch, seq_len, d_model)

    if not pad:
        return x, None

    # mask padded tokens
    mask = torch.zeros(batch, seq_len, dtype=torch.bool)
    mask[0, -2:] = True
    mask[1, -3:] = True

    return x, mask
