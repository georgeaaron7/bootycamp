# -------------------------------------------------------------
# Day 3 - PyTorch Fundamentals (Starter Template)
# Goal:
# Understand PyTorch basics, manipulate tensors, and use autograd
# to define L = f(x, w) and verify gradients.
# -------------------------------------------------------------

import torch
import numpy as np

# =============================================================
# Part A — Basic Tensor Manipulation
# =============================================================

print("\n=== Part A: Basic Tensor Manipulation ===")

# ---------------------------
# 1. Create Tensors
# ---------------------------

print("\n--- Tensor Creation ---")

# Create tensors using:
# - Python lists

arr = [[1, 2, 3], [4, 5, 6]]
t = torch.tensor(arr)
print("Tensor from Python list:", t)
print(f"Shape: {t.shape}, Dtype: {t.dtype}, Device: {t.device}")

# - NumPy arrays

arr_np = np.array(arr)
t_np = torch.tensor(arr_np)
print("\nTensor from NumPy array:", t_np)
print(f"Shape: {t_np.shape}, Dtype: {t_np.dtype}, Device: {t_np.device}")

# - Random tensors (torch.randn)

t_rnd = torch.randn(3, 4)
print("\nRandom Tensor:", t_rnd)
print(f"Shape: {t_rnd.shape}, Dtype: {t_rnd.dtype}, Device: {t_rnd.device}")


# ---------------------------
# 2. Perform Basic Tensor Operations
# ---------------------------

print("\n--- Tensor Operations ---")

# Implement and print results of:
a = torch.tensor([[1, 8], [3, 1]])
b = torch.tensor([[5, 2], [7, 3]])
# - Addition

result = a + b
print("Addition:")
print(result)

# - Multiplication

result = a * b
print("Multiplication:")
print(result)

# - Matrix multiplication (@ or torch.matmul)

result = a @ b
print("Matrix Multiplication:")
print(result)

# - Reshaping (view or reshape)

result_1 = a.view(4)
result_2 = b.reshape(4)
print("Reshaped Tensors:")
print(result_1)
print(result_2)

# - Indexing and slicing

print("Original Tensor:")
print(a)
print("first row:")
print(a[0])
print("second column:")
print(a[:, 1])

# =============================================================
# Part B — Autograd: Define & Verify a Gradient
# =============================================================

print("\n=== Part B: Autograd - Gradient Verification ===")

# TODO:
# - Create tensors with requires_grad=True
# - Define a simple function: L = f(x, w)
#   (You can choose polynomial, dot-product, etc.)
# - Compute output L
# - Call backward(): L.backward()
# - Print gradients using .grad
# - Verify manually if the gradient is correct

x = torch.tensor([2.0, 3.0], requires_grad=True)
w = torch.tensor([4.0, 5.0], requires_grad=True)
L = x.dot(w) + x.pow(2).sum()
print("L:", L)
L.backward()
print("gradient of x:", x.grad)
print("gradient of w:", w.grad)

manual_grad_x = w + 2 * x  
manual_grad_w = x          
print("Manual gradient of x:", manual_grad_x)
print("Manual gradient of w:", manual_grad_w)


# =============================================================
# Expected Output Summary
# =============================================================

print("\n=== Script Must Print ===")
print("1. All created tensors")
print("2. Results of tensor operations")
print("3. Computed gradients using autograd")