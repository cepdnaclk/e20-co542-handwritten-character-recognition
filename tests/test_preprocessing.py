"""
Unit tests for the preprocessing utilities
"""
import unittest
import numpy as np
from PIL import Image
import tempfile
import os
import sys

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from utils.preprocessing import (
    preprocess_image, 
    image_to_array, 
    get_class_name, 
    validate_data_directory,
    calculate_accuracy,
    CLASS_LABELS
)


class TestPreprocessing(unittest.TestCase):
    """Test cases for preprocessing utilities."""
    
    def setUp(self):
        """Set up test fixtures."""
        # Create a temporary test image
        self.test_image = Image.new('L', (64, 64), color=128)
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
        self.test_image.save(self.temp_file.name)
        self.temp_file.close()
    
    def tearDown(self):
        """Clean up test fixtures."""
        os.unlink(self.temp_file.name)
    
    def test_preprocess_image(self):
        """Test image preprocessing."""
        processed = preprocess_image(self.temp_file.name, target_size=(128, 128))
        
        self.assertIsInstance(processed, Image.Image)
        self.assertEqual(processed.size, (128, 128))
        self.assertEqual(processed.mode, 'L')
    
    def test_image_to_array(self):
        """Test image to array conversion."""
        img_array = image_to_array(self.test_image, normalize=True)
        
        self.assertIsInstance(img_array, np.ndarray)
        self.assertEqual(img_array.shape, (64, 64))
        self.assertTrue(0 <= img_array.min() <= 1)
        self.assertTrue(0 <= img_array.max() <= 1)
    
    def test_image_to_array_no_normalize(self):
        """Test image to array conversion without normalization."""
        img_array = image_to_array(self.test_image, normalize=False)
        
        self.assertIsInstance(img_array, np.ndarray)
        self.assertEqual(img_array.shape, (64, 64))
        self.assertTrue(0 <= img_array.min() <= 255)
        self.assertTrue(0 <= img_array.max() <= 255)
    
    def test_get_class_name(self):
        """Test class name retrieval."""
        # Test valid indices
        self.assertEqual(get_class_name(0), '0')
        self.assertEqual(get_class_name(10), 'A')
        
        # Test invalid indices
        self.assertEqual(get_class_name(-1), "Unknown")
        self.assertEqual(get_class_name(len(CLASS_LABELS)), "Unknown")
    
    def test_validate_data_directory_nonexistent(self):
        """Test validation of non-existent directory."""
        result = validate_data_directory('/nonexistent/path')
        self.assertFalse(result)
    
    def test_calculate_accuracy(self):
        """Test accuracy calculation."""
        predictions = np.array([0, 1, 2, 1, 0])
        true_labels = np.array([0, 1, 1, 1, 0])
        
        accuracy = calculate_accuracy(predictions, true_labels)
        self.assertEqual(accuracy, 0.8)  # 4 out of 5 correct
    
    def test_calculate_accuracy_perfect(self):
        """Test accuracy calculation with perfect predictions."""
        predictions = np.array([0, 1, 2, 3])
        true_labels = np.array([0, 1, 2, 3])
        
        accuracy = calculate_accuracy(predictions, true_labels)
        self.assertEqual(accuracy, 1.0)
    
    def test_calculate_accuracy_length_mismatch(self):
        """Test accuracy calculation with mismatched lengths."""
        predictions = np.array([0, 1, 2])
        true_labels = np.array([0, 1])
        
        with self.assertRaises(ValueError):
            calculate_accuracy(predictions, true_labels)
    
    def test_class_labels_count(self):
        """Test that we have the expected number of class labels."""
        self.assertEqual(len(CLASS_LABELS), 47)
        
        # Check that all labels are strings
        for label in CLASS_LABELS:
            self.assertIsInstance(label, str)


if __name__ == '__main__':
    unittest.main()
