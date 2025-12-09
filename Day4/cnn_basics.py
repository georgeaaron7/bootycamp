# -------------------------------------------------------------
# Day 4 - PyTorch Neural Networks (Fixed Version)
# Goal:
# Train a simple FC network and CNN on synthetic shape dataset
# with variability, proper normalization, and Adam optimizer.
# -------------------------------------------------------------

import torch
import torch.nn as nn
import torch.optim as optim
import random
import math

# -------------------------------------------------------------
# Synthetic SHAPE DATASET (3 CLASSES with variability)
# -------------------------------------------------------------
# 0 = circle
# 1 = square
# 2 = triangle

def generate_shape_image(shape_id):
    img = torch.zeros(1, 28, 28)

    # Random translation
    tx = random.randint(-3, 3)
    ty = random.randint(-3, 3)

    # Random rotation
    angle = random.uniform(-30, 30)  # degrees
    theta = math.radians(angle)
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)

    def rotate(i, j, cx, cy):
        x = i - cx
        y = j - cy
        xr = cos_theta*x - sin_theta*y + cx
        yr = sin_theta*x + cos_theta*y + cy
        return int(round(xr)), int(round(yr))

    if shape_id == 0:  # circle
        cx, cy, r = 14 + tx, 14 + ty, random.randint(6, 9)
        for i in range(28):
            for j in range(28):
                x, y = rotate(i, j, cx, cy)
                if 0 <= x < 28 and 0 <= y < 28:
                    if (i - cx)**2 + (j - cy)**2 <= r*r:
                        img[0, x, y] = 1.0

    elif shape_id == 1:  # square
        start, end = 8 + tx, 20 + tx
        start_y, end_y = 8 + ty, 20 + ty
        for i in range(start_y, end_y):
            for j in range(start, end):
                x, y = rotate(i, j, 14, 14)
                if 0 <= x < 28 and 0 <= y < 28:
                    img[0, x, y] = 1.0

    elif shape_id == 2:  # triangle
        top, bottom = 10 + ty, 20 + ty
        for i in range(top, bottom):
            start = 14 - (i - top) + tx
            end   = 14 + (i - top) + tx
            for j in range(start, end):
                x, y = rotate(i, j, 14, 14)
                if 0 <= x < 28 and 0 <= y < 28:
                    img[0, x, y] = 1.0

    # Add small noise and clamp
    img += 0.01 * torch.randn_like(img)
    img = img.clamp(0, 1)
    return img

def generate_dataset(num_samples):
    images, labels = [], []
    for _ in range(num_samples):
        cls = random.randint(0, 2)
        images.append(generate_shape_image(cls))
        labels.append(cls)
    images = torch.stack(images)
    labels = torch.tensor(labels)
    # Normalize to zero mean, unit variance
    images = (images - 0.5) / 0.5
    return images, labels

# Larger train/test sets
train_images, train_labels = generate_dataset(5000)
test_images, test_labels = generate_dataset(1000)

# =============================================================
# Part A — nn.Module Lifecycle
# =============================================================
print("\n=== Part A: nn.Module Lifecycle ===")

class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(28*28, 128)
        self.fc2 = nn.Linear(128, 3)

    def forward(self, x):
        x = x.view(-1, 28*28)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

model = SimpleNN()

print("\nSimpleNN Architecture:")
print(model)
total_params = sum(p.numel() for p in model.parameters())
print(f"Total Parameters: {total_params:,}")

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

for epoch in range(50):
    model.train()
    optimizer.zero_grad()
    outputs = model(train_images)
    loss = criterion(outputs, train_labels)
    loss.backward()
    optimizer.step()
    if (epoch+1) % 10 == 0:
        print(f"Epoch [{epoch+1}/50], Loss: {loss.item():.4f}")

model.eval()
with torch.no_grad():
    outputs = model(test_images)
    _, predicted = torch.max(outputs, 1)
    correct = (predicted == test_labels).sum().item()
    accuracy = 100 * correct / test_labels.size(0)
    print(f"Test Accuracy: {accuracy:.2f}%")

# =============================================================
# Part B — Simple CNN
# =============================================================
print("\n=== Part B: Build a Simple CNN ===")

class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 16, 3, padding=1)
        self.conv2 = nn.Conv2d(16, 32, 3, padding=1)
        self.pool = nn.MaxPool2d(2,2)
        self.fc1 = nn.Linear(32*7*7, 128)
        self.fc2 = nn.Linear(128, 3)

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = self.pool(torch.relu(self.conv2(x)))
        x = x.view(-1, 32*7*7)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

cnn = SimpleCNN()

print("\nSimpleCNN Architecture:")
print(cnn)
total_params = sum(p.numel() for p in cnn.parameters())
print(f"Total Parameters: {total_params:,}")

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(cnn.parameters(), lr=0.001)

for epoch in range(50):
    optimizer.zero_grad()
    outputs = cnn(train_images)
    loss = criterion(outputs, train_labels)
    loss.backward()
    optimizer.step()
    if (epoch+1) % 10 == 0:
        print(f"Epoch [{epoch+1}/50], Loss: {loss.item():.4f}")

cnn.eval()
with torch.no_grad():
    outputs = cnn(test_images)
    _, predicted = torch.max(outputs, 1)
    correct = (predicted == test_labels).sum().item()
    accuracy = 100 * correct / test_labels.size(0)
    print(f"Test Accuracy: {accuracy:.2f}%")

# =============================================================
# Output
# =============================================================
print("\n=== Script Must Print ===")
print("1. Model architecture")
print("2. Number of parameters")
print("3. Training and evaluation results")
