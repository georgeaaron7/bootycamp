import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F # For ReLU function

# =============================================================
# Part A — nn.Module Lifecycle
# =============================================================

print("\n=== Part A: nn.Module Lifecycle ===")

# Simple Model
class SimpleModel(nn.Module):
    def __init__(self):
        super().__init__()
        
        # These are the 3 layers
        self.layer1 = nn.Linear(20,64)
        self.layer2 = nn.Linear(64,32)
        self.layer3 = nn.Linear(32,5)

    def forward(self, x):
        # Flow of data
        x = torch.relu(self.layer1(x))
        x = torch.relu(self.layer2(x))
        x = self.layer3(x)
  
        return x

# Instantiate and Inspect
model = SimpleModel()
print(model) # Model Architecture

parameters = sum(p.numel() for p in model.parameters())
print("Total parameters: ", parameters) # Model Parameters

# Random Data
X = torch.randn(200, 20) 
y = torch.randint(0, 5, (200,))

# Training 
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

print("\nTraining Now")

for epoch in range(5):
    optimizer.zero_grad()

    outputs = model(X)   # forward pass
    loss = criterion(outputs, y)

    loss.backward()      # compute gradients
    optimizer.step()     # update weights

    print(f"Epoch {epoch+1} | Loss = {loss.item():.4f}")

# Evaluation

model.eval()
with torch.no_grad():
    outputs = model(X)
    preds = outputs.argmax(dim=1)
    accuracy = (preds == y).float().mean()

print("\nEvaluation Accuracy:", accuracy.item())


# =============================================================
# Part B — Build a Simple CNN
# =============================================================

print("\n=== Part B: Build a Simple CNN ===")

# Simple CNN Model
class SimpleCNN(nn.Module):
    def __init__(self):
        super().__init__()
        # Convolution layer:
        # 1 Input channels, 8 Output channels (filters)
        # Kernel size = 3x3
        self.conv1 = nn.Conv2d(1,8,3)
        self.pool = nn.MaxPool2d(2,2)
        self.conv2 = nn.Conv2d(8,16,3)
        self.fc = nn.Linear(16 * 5 * 5, 10)

    def forward(self, x):
        x = torch.relu(self.conv1(x))
        x = self.pool(x)
        x = torch.relu(self.conv2(x))
        x = self.pool(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x

# Model Instantiation   
cnn = SimpleCNN()
print(cnn)

cnn_params = sum(p.numel() for p in cnn.parameters())
print("\nTotal CNN parameters:", cnn_params)

# Dummy Data
X_img = torch.randn(500, 1, 28, 28)
y_img = torch.randint(0, 10, (500,))

# Training
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(cnn.parameters(), lr=0.001)

print("\nTraining CNN...")
for epoch in range(5):
    optimizer.zero_grad()
    
    outputs = cnn(X_img)
    loss = criterion(outputs, y_img)
    
    loss.backward()
    optimizer.step()
    
    print(f"Epoch {epoch+1} | Loss = {loss.item():.4f}")

# Evaluation
cnn.eval()
with torch.no_grad():
    outputs = cnn(X_img)
    preds = outputs.argmax(dim=1)
    acc = (preds == y_img).float().mean()

print("\nCNN Accuracy:", acc.item())
