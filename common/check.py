import torch
import torchvision

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print(f"torch: {torch.__version__}")
print(f"torchvision: {torchvision.__version__}")
print(f"device: {device}")
