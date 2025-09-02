"""
Main entry point for the SD19 Handwritten Character Recognition system.
This script provides a command-line interface to various functionalities.

Authors: Sandalu Umayanga (E/20/284), Milinda Perera (E/20/286), 
         Sampath K.G.H. (E/19/490), Nadeeka Dissanayake (E/20/078)
Course: CO542 Neural Networks and Fuzzy Systems
Institution: University of Peradeniya, Department of Computer Engineering
"""
import argparse
import sys
import os

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.gui.application import main as gui_main


def train_pytorch():
    """Train PyTorch model."""
    from scripts.train_pytorch import main
    main()


def train_keras():
    """Train Keras model."""
    from scripts.train_keras import main
    main()


def predict_image(image_path, model_path, model_type='pytorch'):
    """Predict character from image file."""
    from src.utils.prediction import ModelPredictor
    
    if model_type == 'pytorch':
        from src.models.pytorch_model import load_model
        model = load_model(model_path)
    else:
        from src.models.keras_model import load_keras_model
        model = load_keras_model(model_path)
    
    predictor = ModelPredictor(model, model_type)
    predicted_class, confidence = predictor.predict_image(image_path)
    
    print(f"Predicted: {predicted_class}")
    print(f"Confidence: {confidence:.2%}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="SD19 Handwritten Character Recognition System"
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # GUI command
    gui_parser = subparsers.add_parser('gui', help='Launch GUI application')
    gui_parser.add_argument('--model', help='Path to model file')
    gui_parser.add_argument('--type', choices=['pytorch', 'tensorflow'], 
                           default='pytorch', help='Model type')
    
    # Training commands
    train_parser = subparsers.add_parser('train', help='Train a model')
    train_parser.add_argument('framework', choices=['pytorch', 'keras'], 
                             help='Framework to use')
    
    # Prediction command
    predict_parser = subparsers.add_parser('predict', help='Predict from image')
    predict_parser.add_argument('image', help='Path to image file')
    predict_parser.add_argument('model', help='Path to model file')
    predict_parser.add_argument('--type', choices=['pytorch', 'tensorflow'], 
                               default='pytorch', help='Model type')
    
    args = parser.parse_args()
    
    if args.command == 'gui':
        gui_main()
    elif args.command == 'train':
        if args.framework == 'pytorch':
            train_pytorch()
        else:
            train_keras()
    elif args.command == 'predict':
        predict_image(args.image, args.model, args.type)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
