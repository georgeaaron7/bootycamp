import torch
import numpy as np

print("\n=== Part A: Basic Tensor Manipulation ===")

# -------------------------------------------------
# Tensor Creation
# -------------------------------------------------
print("\n--- Tensor Creation ---")

data = [[1, 2], [3, 4]]
x_data = torch.tensor(data)
print(f"Shape: {x_data.shape}, Dtype: {x_data.dtype}, Device: {x_data.device}")

data_2 = [[1, 2, 3], [3, 4, 5]]
np_array = np.array(data)
x_np = torch.from_numpy(np_array)
print(f"Shape: {np_array.shape}, Dtype: {np_array.dtype}, Device: {np_array.device}")

shape = (3, 4)
rand_tensor = torch.rand(shape)
print(f"Shape: {rand_tensor.shape}, Dtype: {rand_tensor.dtype}, Device: {rand_tensor.device}")

tensor_1 = torch.tensor([[1, 2, 3],
                         [4, 5, 6]])

tensor_2 = torch.tensor([[7, 8, 9],
                         [1, 2, 3]])

# -------------------------------------------------
# Tensor Operations
# -------------------------------------------------
print("\n--- Tensor Operations ---")

print(tensor_1 + tensor_2)      # addition
print(tensor_1 * tensor_2)      # element-wise multiplication

tensor_3 = torch.tensor([[1, 2],
                         [3, 4],
                         [5, 6]])

print(torch.matmul(tensor_1, tensor_3))   # matrix multiplication

# Reshaping
tensor_4 = torch.arange(1, 13)
print(tensor_4.view(3, 4))

# Indexing & Slicing
X = torch.tensor([[11, 20, 30],
                  [40, 53, 66],
                  [70, 85, 90]])

print("\nX:\n", X)
print(f"Single element X[1,2] = {X[1, 2]}")
print(f"Row 0: {X[0]}")
print(f"Column 1: {X[:, 1]}")
print(f"Submatrix X[0:2, 1:3]:\n{X[0:2, 1:3]}")

# -------------------------------------------------
# Autograd Section
# -------------------------------------------------
x = torch.tensor([[1.0, 2.0],
                  [3.0, 4.0]], requires_grad=True)

w = torch.tensor([[2.0, 1.0],
                  [0.0, 3.0]], requires_grad=True)

print("\nTensor x:\n", x)
print("Tensor w:\n", w)

L = torch.sum(x * w)
print("\nComputed L:", L.item())

L.backward()

print("\ngradient of L with x:\n", x.grad)
print("\ngradient of L with w:\n", w.grad)

print("\ngradient wrt x = w")
print("Expected:\n", w)

print("\ngradient wrt w = x")
print(x)
