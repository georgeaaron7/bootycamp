# Day 4: PyTorch Neural Networks — nn.Module & CNNs

Day 4 builds upon your understanding of PyTorch by diving into neural networks and convolutional layers. Today, you will explore the lifecycle of `nn.Module`, and learn how to use `nn.Conv2d` and `nn.MaxPool2d` to build convolutional neural networks (CNNs).

---

## 🧪 Main Goal
The ultimate goal is to understand the `nn.Module` lifecycle and implement a simple CNN using `nn.Conv2d` and `nn.MaxPool2d`. You will also learn how to structure your PyTorch models effectively.

## 🧠 Task 1: Conceptual Understanding

Before writing any code, you must understand the core PyTorch concepts. Study the following resources completely:

**PyTorch Official Docs — What is nn.Module?**  
https://pytorch.org/docs/stable/generated/torch.nn.Module.html

**Blog — Understanding nn.Conv2d and nn.MaxPool2d**  
https://towardsdatascience.com/convolutional-neural-networks-explained-9cc5188c4939

**Video — CNNs Explained**  
https://www.youtube.com/watch?v=YRhxdVk_sIs

## 🐍 Task 2: Hands-On Implementation (Python)

You will now write a script to practice `nn.Module` and CNNs.
Navigate to your Day-04 folder:

```bash
cd Day4/
```
Inside this folder, create the following Python file:
```bash
cnn_basics.py
```

---

Inside this script, you must complete two core tasks:

🔹 **Part A — nn.Module Lifecycle**

To understand the lifecycle of `nn.Module`, implement the following:

1. **Define a Simple Model**

Create a class that inherits from `nn.Module` and implements:

• `__init__` method to define layers

• `forward` method to define the forward pass

2. **Instantiate and Inspect the Model**

• Print the model architecture

• Print the number of parameters

3. **Train and Evaluate Lifecycle**

• Define a dummy dataset

• Train the model for a few epochs

• Evaluate the model

---

🔹 **Part B — Build a Simple CNN**

The main objective is to use `nn.Conv2d` and `nn.MaxPool2d` to build a CNN.

You must:

• Define a CNN class with convolutional and pooling layers

• Use `nn.Conv2d` for convolutional layers

• Use `nn.MaxPool2d` for pooling layers

• Add a fully connected layer at the end

• Train the CNN on a dummy dataset

📤 **What Your Script Must Print**

Your script must display:
1. The model architecture
2. The number of parameters
3. Training and evaluation results

---

If needed, you can use this template and fill in the TODO sections to complete the exercises
## ✍️Template 
```bash
# -------------------------------------------------------------
# Day 4 - PyTorch Neural Networks (Starter Template)
# Goal:
# Understand nn.Module lifecycle, build a CNN using nn.Conv2d
# and nn.MaxPool2d, and train it on a dummy dataset.
# -------------------------------------------------------------

import torch
import torch.nn as nn
import torch.optim as optim

# =============================================================
# Part A — nn.Module Lifecycle
# =============================================================

print("\n=== Part A: nn.Module Lifecycle ===")

# ---------------------------
# 1. Define a Simple Model
# ---------------------------

# TODO: Define a class that inherits from nn.Module

# ---------------------------
# 2. Instantiate and Inspect the Model
# ---------------------------

# TODO: Instantiate the model and print architecture

# ---------------------------
# 3. Train and Evaluate Lifecycle
# ---------------------------

# TODO: Train the model on a dummy dataset

# =============================================================
# Part B — Build a Simple CNN
# =============================================================

print("\n=== Part B: Build a Simple CNN ===")

# TODO: Define a CNN class with nn.Conv2d and nn.MaxPool2d

# TODO: Train the CNN on a dummy dataset

# =============================================================
# Expected Output Summary
# =============================================================

print("\n=== Script Must Print ===")
print("1. Model architecture")
print("2. Number of parameters")
print("3. Training and evaluation results")
```

## 💾 Task 3: Submission Using Feature Branching

Follow the exact Git workflow used in Day 1, Day 2, and Day 3.

**1. Synchronization & Branch Creation**

Create Day4 folder (if not already there). If it's already created, navigate into it using:
```bash
cd Day4/
```

1. Switch to `main`:

```bash
git checkout main
```

2. Pull latest instructions:
```bash
git pull upstream main
```

3. Create your Day4 branch:
```bash
git checkout -b feat/day4-<your-name>
```

**2. Complete Task & Commit**

After finishing `cnn_basics.py`:
```bash
git add .
git commit -m "feat(day04): Implemented nn.Module lifecycle and CNN basics"
```
**3. Push Your Branch**
```bash
git push -u origin feat/day4-<your-name>
```
**4. Open the Pull Request (PR)**

1. Go to your fork on GitHub

2. Click Compare & Pull Request

3. Ensure source/destination is correct:

• From: your branch

• To: main branch of the original bootcamp repo

4. PR Title Format
```
[D04] <Your Name> - nn.Module & CNN Implementation
```

5. PR Description Must Include

• Defined a simple model using nn.Module

• Built a CNN using nn.Conv2d and nn.MaxPool2d

• Trained and evaluated the model

• File located inside Day4/

6. Click Create Pull Request.
