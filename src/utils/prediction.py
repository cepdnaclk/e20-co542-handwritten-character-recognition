"""
Prediction utilities for both PyTorch and TensorFlow models
"""
import numpy as np
from PIL import Image
from .preprocessing import preprocess_image, image_to_array, get_class_name


class ModelPredictor:
    """
    Unified predictor class for both PyTorch and TensorFlow models.
    """
    
    def __init__(self, model, model_type='pytorch'):
        """
        Initialize the predictor.
        
        Args:
            model: Trained model (PyTorch or TensorFlow)
            model_type (str): Type of model ('pytorch' or 'tensorflow')
        """
        self.model = model
        self.model_type = model_type.lower()
        
        if self.model_type not in ['pytorch', 'tensorflow']:
            raise ValueError("model_type must be 'pytorch' or 'tensorflow'")
    
    def predict_image(self, image_path):
        """
        Predict the character in an image file.
        
        Args:
            image_path (str): Path to the image file
            
        Returns:
            tuple: (predicted_class, confidence)
        """
        # Preprocess image
        image = preprocess_image(image_path)
        img_array = image_to_array(image)
        
        return self._predict_array(img_array)
    
    def predict_pil_image(self, pil_image):
        """
        Predict the character in a PIL Image.
        
        Args:
            pil_image (PIL.Image): PIL Image object
            
        Returns:
            tuple: (predicted_class, confidence)
        """
        # Convert to array
        img_array = image_to_array(pil_image)
        
        return self._predict_array(img_array)
    
    def _predict_array(self, img_array):
        """
        Internal method to make predictions from numpy array.
        
        Args:
            img_array (numpy.ndarray): Image array
            
        Returns:
            tuple: (predicted_class, confidence)
        """
        if self.model_type == 'pytorch':
            return self._predict_pytorch(img_array)
        else:
            return self._predict_tensorflow(img_array)
    
    def _predict_pytorch(self, img_array):
        """
        Make prediction using PyTorch model.
        
        Args:
            img_array (numpy.ndarray): Image array
            
        Returns:
            tuple: (predicted_class, confidence)
        """
        import torch
        
        # Reshape for PyTorch (batch_size, channels, height, width)
        img_tensor = torch.FloatTensor(img_array).unsqueeze(0).unsqueeze(0)
        
        with torch.no_grad():
            outputs = self.model(img_tensor)
            probabilities = torch.softmax(outputs, dim=1)
            confidence, predicted = torch.max(probabilities, 1)
            
            predicted_class = get_class_name(predicted.item())
            confidence_score = confidence.item()
            
            return predicted_class, confidence_score
    
    def _predict_tensorflow(self, img_array):
        """
        Make prediction using TensorFlow model.
        
        Args:
            img_array (numpy.ndarray): Image array
            
        Returns:
            tuple: (predicted_class, confidence)
        """
        # Reshape for TensorFlow (batch_size, height, width, channels)
        img_tensor = np.expand_dims(np.expand_dims(img_array, axis=0), axis=-1)
        
        predictions = self.model.predict(img_tensor)
        predicted_index = np.argmax(predictions[0])
        confidence_score = np.max(predictions[0])
        
        predicted_class = get_class_name(predicted_index)
        
        return predicted_class, confidence_score
    
    def predict_batch(self, image_paths):
        """
        Predict characters for a batch of images.
        
        Args:
            image_paths (list): List of image file paths
            
        Returns:
            list: List of (predicted_class, confidence) tuples
        """
        results = []
        for image_path in image_paths:
            try:
                result = self.predict_image(image_path)
                results.append(result)
            except Exception as e:
                print(f"Error processing {image_path}: {e}")
                results.append(("Error", 0.0))
        
        return results
