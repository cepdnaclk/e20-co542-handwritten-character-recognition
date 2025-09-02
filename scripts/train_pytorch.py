"""
Training script for PyTorch model
"""
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms
import os
import sys
from PIL import Image
import numpy as np

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.models.pytorch_model import SD19Model
from src.utils.preprocessing import CLASS_LABELS, validate_data_directory


class SD19Dataset(Dataset):
    """Custom dataset for SD19 character images."""
    
    def __init__(self, data_dir, transform=None):
        """
        Initialize dataset.
        
        Args:
            data_dir (str): Path to data directory
            transform: Image transformations
        """
        self.data_dir = data_dir
        self.transform = transform
        self.samples = []
        self.class_to_idx = {label: idx for idx, label in enumerate(CLASS_LABELS)}
        
        self._load_samples()
    
    def _load_samples(self):
        """Load all image samples and their labels."""
        for class_name in os.listdir(self.data_dir):
            class_path = os.path.join(self.data_dir, class_name)
            if os.path.isdir(class_path) and class_name in self.class_to_idx:
                class_idx = self.class_to_idx[class_name]
                
                for img_name in os.listdir(class_path):
                    if img_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                        img_path = os.path.join(class_path, img_name)
                        self.samples.append((img_path, class_idx))
    
    def __len__(self):
        return len(self.samples)
    
    def __getitem__(self, idx):
        img_path, label = self.samples[idx]
        
        # Load and preprocess image
        image = Image.open(img_path).convert('L')
        
        if self.transform:
            image = self.transform(image)
        
        return image, label


def get_data_loaders(data_dir, batch_size=32, validation_split=0.2):
    """
    Create data loaders for training and validation.
    
    Args:
        data_dir (str): Path to data directory
        batch_size (int): Batch size
        validation_split (float): Validation split ratio
        
    Returns:
        tuple: (train_loader, val_loader)
    """
    transform = transforms.Compose([
        transforms.Resize((128, 128)),
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])
    
    # Create full dataset
    full_dataset = SD19Dataset(data_dir, transform=transform)
    
    # Split into train and validation
    dataset_size = len(full_dataset)
    val_size = int(validation_split * dataset_size)
    train_size = dataset_size - val_size
    
    train_dataset, val_dataset = torch.utils.data.random_split(
        full_dataset, [train_size, val_size]
    )
    
    # Create data loaders
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)
    
    return train_loader, val_loader


def train_model(model, train_loader, val_loader, num_epochs=50, learning_rate=0.001, device='cpu'):
    """
    Train the PyTorch model.
    
    Args:
        model: PyTorch model to train
        train_loader: Training data loader
        val_loader: Validation data loader
        num_epochs (int): Number of training epochs
        learning_rate (float): Learning rate
        device (str): Device to train on
        
    Returns:
        dict: Training history
    """
    model.to(device)
    
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.1)
    
    history = {'train_loss': [], 'train_acc': [], 'val_loss': [], 'val_acc': []}
    
    best_val_acc = 0.0
    
    for epoch in range(num_epochs):
        # Training phase
        model.train()
        train_loss = 0.0
        train_correct = 0
        train_total = 0
        
        for batch_idx, (data, target) in enumerate(train_loader):
            data, target = data.to(device), target.to(device)
            
            optimizer.zero_grad()
            output = model(data)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()
            
            train_loss += loss.item()
            _, predicted = torch.max(output.data, 1)
            train_total += target.size(0)
            train_correct += (predicted == target).sum().item()
            
            if batch_idx % 100 == 0:
                print(f'Epoch {epoch+1}/{num_epochs}, Batch {batch_idx}, '
                      f'Loss: {loss.item():.4f}')
        
        # Validation phase
        model.eval()
        val_loss = 0.0
        val_correct = 0
        val_total = 0
        
        with torch.no_grad():
            for data, target in val_loader:
                data, target = data.to(device), target.to(device)
                output = model(data)
                loss = criterion(output, target)
                
                val_loss += loss.item()
                _, predicted = torch.max(output.data, 1)
                val_total += target.size(0)
                val_correct += (predicted == target).sum().item()
        
        # Calculate metrics
        train_loss /= len(train_loader)
        train_acc = train_correct / train_total
        val_loss /= len(val_loader)
        val_acc = val_correct / val_total
        
        # Update history
        history['train_loss'].append(train_loss)
        history['train_acc'].append(train_acc)
        history['val_loss'].append(val_loss)
        history['val_acc'].append(val_acc)
        
        # Step scheduler
        scheduler.step()
        
        print(f'Epoch {epoch+1}/{num_epochs}:')
        print(f'Train Loss: {train_loss:.4f}, Train Acc: {train_acc:.4f}')
        print(f'Val Loss: {val_loss:.4f}, Val Acc: {val_acc:.4f}')
        print('-' * 50)
        
        # Save best model
        if val_acc > best_val_acc:
            best_val_acc = val_acc
            torch.save(model.state_dict(), 'best_pytorch_model.pth')
            print(f'New best model saved with validation accuracy: {val_acc:.4f}')
    
    return history


def main():
    """Main training function."""
    # Configuration
    DATA_DIR = 'data/by_merge'  # Update this path
    BATCH_SIZE = 32
    NUM_EPOCHS = 50
    LEARNING_RATE = 0.001
    DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    print(f"Using device: {DEVICE}")
    
    # Validate data directory
    if not validate_data_directory(DATA_DIR):
        print("Please ensure the data directory exists and contains class subdirectories")
        return
    
    # Create data loaders
    print("Creating data loaders...")
    train_loader, val_loader = get_data_loaders(DATA_DIR, BATCH_SIZE)
    
    print(f"Training samples: {len(train_loader.dataset)}")
    print(f"Validation samples: {len(val_loader.dataset)}")
    
    # Create model
    model = SD19Model(num_classes=len(CLASS_LABELS))
    print(f"Model created with {len(CLASS_LABELS)} classes")
    
    # Train model
    print("Starting training...")
    history = train_model(model, train_loader, val_loader, NUM_EPOCHS, LEARNING_RATE, DEVICE)
    
    # Save final model
    torch.save(model.state_dict(), 'final_pytorch_model.pth')
    print("Training completed! Final model saved as 'final_pytorch_model.pth'")


if __name__ == "__main__":
    main()
