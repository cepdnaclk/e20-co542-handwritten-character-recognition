# API Documentation

## Overview

This document provides detailed information about the API and class interfaces available in the SD19 Handwritten Character Recognition system.

## Models Module

### PyTorch Model (`src/models/pytorch_model.py`)

#### SD19Model Class

```python
class SD19Model(nn.Module):
    def __init__(self, num_classes=47):
        """
        Initialize the SD19 model.
        
        Args:
            num_classes (int): Number of character classes to classify
        """
```

**Methods:**

- `forward(x)`: Forward pass through the network
- `_init_linear()`: Calculate flattened feature size

#### Functions

- `get_transform()`: Returns preprocessing transform pipeline
- `load_model(model_path, device='cpu')`: Load trained PyTorch model

### Keras Model (`src/models/keras_model.py`)

#### Functions

- `create_sd19_model(input_shape=(128, 128, 1), num_classes=47)`: Create CNN model
- `create_data_generators(data_dir, batch_size=128, validation_split=0.2)`: Create data generators
- `load_keras_model(model_path)`: Load trained Keras model

## Utils Module

### Preprocessing (`src/utils/preprocessing.py`)

#### Constants

- `CLASS_LABELS`: List of 47 character class labels

#### Functions

```python
def preprocess_image(image_path, target_size=(128, 128)):
    """
    Preprocess an image for model prediction.
    
    Args:
        image_path (str): Path to the image file
        target_size (tuple): Target size for the image (width, height)
        
    Returns:
        PIL.Image: Preprocessed image
    """

def image_to_array(image, normalize=True):
    """
    Convert PIL Image to numpy array.
    
    Args:
        image (PIL.Image): Input image
        normalize (bool): Whether to normalize pixel values to [0, 1]
        
    Returns:
        numpy.ndarray: Image array
    """

def get_class_name(class_index):
    """
    Get the class name from class index.
    
    Args:
        class_index (int): Index of the predicted class
        
    Returns:
        str: Class name/label
    """

def validate_data_directory(data_dir):
    """
    Validate that the data directory exists and contains subdirectories.
    
    Args:
        data_dir (str): Path to the data directory
        
    Returns:
        bool: True if valid, False otherwise
    """

def calculate_accuracy(predictions, true_labels):
    """
    Calculate accuracy from predictions and true labels.
    
    Args:
        predictions (numpy.ndarray): Model predictions
        true_labels (numpy.ndarray): True labels
        
    Returns:
        float: Accuracy score
    """
```

### Prediction (`src/utils/prediction.py`)

#### ModelPredictor Class

```python
class ModelPredictor:
    def __init__(self, model, model_type='pytorch'):
        """
        Initialize the predictor.
        
        Args:
            model: Trained model (PyTorch or TensorFlow)
            model_type (str): Type of model ('pytorch' or 'tensorflow')
        """
```

**Methods:**

```python
def predict_image(self, image_path):
    """
    Predict the character in an image file.
    
    Args:
        image_path (str): Path to the image file
        
    Returns:
        tuple: (predicted_class, confidence)
    """

def predict_pil_image(self, pil_image):
    """
    Predict the character in a PIL Image.
    
    Args:
        pil_image (PIL.Image): PIL Image object
        
    Returns:
        tuple: (predicted_class, confidence)
    """

def predict_batch(self, image_paths):
    """
    Predict characters for a batch of images.
    
    Args:
        image_paths (list): List of image file paths
        
    Returns:
        list: List of (predicted_class, confidence) tuples
    """
```

## GUI Module

### Application (`src/gui/application.py`)

#### HandwritingApp Class

```python
class HandwritingApp:
    def __init__(self, master, model_path=None, model_type='pytorch'):
        """
        Initialize the GUI application.
        
        Args:
            master: Tkinter root window
            model_path (str): Path to the trained model
            model_type (str): Type of model ('pytorch' or 'tensorflow')
        """
```

**Key Methods:**

- `load_model(model_path, model_type)`: Load a trained model
- `predict_character()`: Predict character from canvas drawing
- `upload_image()`: Upload and predict an image file
- `clear_canvas()`: Clear the drawing canvas

## Training Scripts

### PyTorch Training (`scripts/train_pytorch.py`)

#### SD19Dataset Class

```python
class SD19Dataset(Dataset):
    def __init__(self, data_dir, transform=None):
        """
        Initialize dataset.
        
        Args:
            data_dir (str): Path to data directory
            transform: Image transformations
        """
```

#### Functions

```python
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
```

### Keras Training (`scripts/train_keras.py`)

#### Functions

```python
def plot_training_history(history, save_path='training_history.png'):
    """
    Plot training history.
    
    Args:
        history: Keras training history
        save_path (str): Path to save the plot
    """

def train_model(data_dir, model_save_path='keras_model.h5', epochs=50, batch_size=32):
    """
    Train the Keras model.
    
    Args:
        data_dir (str): Path to training data
        model_save_path (str): Path to save the trained model
        epochs (int): Number of training epochs
        batch_size (int): Training batch size
        
    Returns:
        tf.keras.Model: Trained model
    """
```

## Usage Examples

### Basic Prediction

```python
from src.models.pytorch_model import load_model
from src.utils.prediction import ModelPredictor

# Load model
model = load_model('saved_models/sd19_model.pth')
predictor = ModelPredictor(model, 'pytorch')

# Single prediction
predicted_class, confidence = predictor.predict_image('test_image.png')
print(f"Predicted: {predicted_class} (Confidence: {confidence:.2%})")

# Batch prediction
image_files = ['img1.png', 'img2.png', 'img3.png']
results = predictor.predict_batch(image_files)
for i, (pred, conf) in enumerate(results):
    print(f"Image {i+1}: {pred} ({conf:.2%})")
```

### Custom Training

```python
from scripts.train_pytorch import get_data_loaders, train_model
from src.models.pytorch_model import SD19Model

# Setup data
train_loader, val_loader = get_data_loaders('data/by_merge', batch_size=64)

# Create model
model = SD19Model(num_classes=47)

# Train
history = train_model(
    model=model,
    train_loader=train_loader,
    val_loader=val_loader,
    num_epochs=25,
    learning_rate=0.001,
    device='cuda'
)
```

### GUI Integration

```python
import tkinter as tk
from src.gui.application import HandwritingApp

# Create GUI with pre-loaded model
root = tk.Tk()
app = HandwritingApp(
    master=root,
    model_path='saved_models/sd19_model.pth',
    model_type='pytorch'
)
root.mainloop()
```

## Error Handling

### Common Exceptions

- `FileNotFoundError`: Model file or image not found
- `ValueError`: Invalid model type or incompatible dimensions
- `ImportError`: Missing dependencies (torch, tensorflow, etc.)
- `RuntimeError`: CUDA/GPU related issues

### Best Practices

1. Always check if model is loaded before prediction
2. Validate input image format and size
3. Handle GPU memory issues gracefully
4. Provide meaningful error messages to users

## Performance Considerations

### Memory Usage

- Model loading: ~50MB RAM
- Single prediction: ~10MB additional RAM
- Batch prediction: Scales with batch size

### Optimization Tips

1. Use GPU when available for faster inference
2. Batch multiple predictions for efficiency
3. Preprocess images in advance when possible
4. Consider model quantization for deployment
