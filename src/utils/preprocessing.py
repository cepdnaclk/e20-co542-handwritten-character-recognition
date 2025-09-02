"""
Utility functions for data preprocessing and image handling
"""
import numpy as np
from PIL import Image, ImageOps
import os


# SD19 dataset class labels
CLASS_LABELS = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'A', 'B', 'C.c', 'D', 'E', 'F', 'G', 'H', 'I.i', 'J.j',
    'K.k', 'L.l', 'M.m', 'N', 'O.o', 'P.p', 'Q', 'R', 'S.s',
    'T', 'U.u', 'V.v', 'W.w', 'X.x', 'Y.y', 'Z.z',
    'a', 'b', 'd', 'e', 'f', 'g', 'h', 'n', 'q', 'r', 't'
]


def preprocess_image(image_path, target_size=(128, 128)):
    """
    Preprocess an image for model prediction.
    
    Args:
        image_path (str): Path to the image file
        target_size (tuple): Target size for the image (width, height)
        
    Returns:
        PIL.Image: Preprocessed image
    """
    # Open and convert to grayscale
    image = Image.open(image_path).convert('L')
    
    # Invert colors if necessary (white background, black text)
    image = ImageOps.invert(image)
    
    # Resize image
    image = image.resize(target_size, Image.LANCZOS)
    
    return image


def preprocess_canvas_image(canvas_data, target_size=(128, 128)):
    """
    Preprocess image data from a canvas for model prediction.
    
    Args:
        canvas_data: Canvas image data
        target_size (tuple): Target size for the image (width, height)
        
    Returns:
        PIL.Image: Preprocessed image
    """
    # Convert canvas data to PIL Image
    image = Image.fromarray(canvas_data).convert('L')
    
    # Resize image
    image = image.resize(target_size, Image.LANCZOS)
    
    return image


def image_to_array(image, normalize=True):
    """
    Convert PIL Image to numpy array.
    
    Args:
        image (PIL.Image): Input image
        normalize (bool): Whether to normalize pixel values to [0, 1]
        
    Returns:
        numpy.ndarray: Image array
    """
    img_array = np.array(image)
    
    if normalize:
        img_array = img_array.astype(np.float32) / 255.0
    
    return img_array


def get_class_name(class_index):
    """
    Get the class name from class index.
    
    Args:
        class_index (int): Index of the predicted class
        
    Returns:
        str: Class name/label
    """
    if 0 <= class_index < len(CLASS_LABELS):
        return CLASS_LABELS[class_index]
    else:
        return "Unknown"


def validate_data_directory(data_dir):
    """
    Validate that the data directory exists and contains subdirectories.
    
    Args:
        data_dir (str): Path to the data directory
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not os.path.exists(data_dir):
        print(f"Error: Data directory {data_dir} does not exist")
        return False
    
    subdirs = [d for d in os.listdir(data_dir) 
               if os.path.isdir(os.path.join(data_dir, d))]
    
    if len(subdirs) == 0:
        print(f"Error: No subdirectories found in {data_dir}")
        return False
    
    print(f"Found {len(subdirs)} classes in data directory")
    return True


def calculate_accuracy(predictions, true_labels):
    """
    Calculate accuracy from predictions and true labels.
    
    Args:
        predictions (numpy.ndarray): Model predictions
        true_labels (numpy.ndarray): True labels
        
    Returns:
        float: Accuracy score
    """
    if len(predictions) != len(true_labels):
        raise ValueError("Predictions and true labels must have the same length")
    
    correct = np.sum(predictions == true_labels)
    total = len(predictions)
    
    return correct / total
