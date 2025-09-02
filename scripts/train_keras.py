"""
Training script for TensorFlow/Keras model
"""
import tensorflow as tf
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
import os
import sys
import matplotlib.pyplot as plt

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.models.keras_model import create_sd19_model, create_data_generators
from src.utils.preprocessing import validate_data_directory


def plot_training_history(history, save_path='training_history.png'):
    """
    Plot training history.
    
    Args:
        history: Keras training history
        save_path (str): Path to save the plot
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    
    # Plot training & validation accuracy
    ax1.plot(history.history['accuracy'], label='Training Accuracy')
    ax1.plot(history.history['val_accuracy'], label='Validation Accuracy')
    ax1.set_title('Model Accuracy')
    ax1.set_xlabel('Epoch')
    ax1.set_ylabel('Accuracy')
    ax1.legend()
    ax1.grid(True)
    
    # Plot training & validation loss
    ax2.plot(history.history['loss'], label='Training Loss')
    ax2.plot(history.history['val_loss'], label='Validation Loss')
    ax2.set_title('Model Loss')
    ax2.set_xlabel('Epoch')
    ax2.set_ylabel('Loss')
    ax2.legend()
    ax2.grid(True)
    
    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()
    print(f"Training history plot saved as {save_path}")


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
    # Validate data directory
    if not validate_data_directory(data_dir):
        raise ValueError("Invalid data directory")
    
    # Create data generators
    print("Creating data generators...")
    train_generator, val_generator = create_data_generators(data_dir, batch_size)
    
    print(f"Training samples: {train_generator.samples}")
    print(f"Validation samples: {val_generator.samples}")
    print(f"Number of classes: {train_generator.num_classes}")
    
    # Create model
    model = create_sd19_model(num_classes=train_generator.num_classes)
    
    # Print model summary
    print("\nModel Architecture:")
    model.summary()
    
    # Define callbacks
    callbacks = [
        ModelCheckpoint(
            model_save_path,
            monitor='val_accuracy',
            save_best_only=True,
            mode='max',
            verbose=1
        ),
        EarlyStopping(
            monitor='val_loss',
            patience=10,
            restore_best_weights=True,
            verbose=1
        ),
        ReduceLROnPlateau(
            monitor='val_loss',
            factor=0.2,
            patience=5,
            min_lr=0.0001,
            verbose=1
        )
    ]
    
    # Train model
    print("\nStarting training...")
    history = model.fit(
        train_generator,
        steps_per_epoch=train_generator.samples // batch_size,
        epochs=epochs,
        validation_data=val_generator,
        validation_steps=val_generator.samples // batch_size,
        callbacks=callbacks,
        verbose=1
    )
    
    # Plot training history
    plot_training_history(history)
    
    # Evaluate model
    print("\nEvaluating model on validation data...")
    val_loss, val_accuracy = model.evaluate(val_generator, verbose=1)
    print(f"Validation Loss: {val_loss:.4f}")
    print(f"Validation Accuracy: {val_accuracy:.4f}")
    
    return model, history


def main():
    """Main training function."""
    # Configuration
    DATA_DIR = 'data/by_merge'  # Update this path
    MODEL_SAVE_PATH = 'trained_keras_model.h5'
    EPOCHS = 50
    BATCH_SIZE = 32
    
    # Check if GPU is available
    print("GPU Available: ", tf.config.list_physical_devices('GPU'))
    
    try:
        # Train model
        model, history = train_model(
            data_dir=DATA_DIR,
            model_save_path=MODEL_SAVE_PATH,
            epochs=EPOCHS,
            batch_size=BATCH_SIZE
        )
        
        print(f"\nTraining completed successfully!")
        print(f"Model saved as: {MODEL_SAVE_PATH}")
        
        # Save training history
        import pickle
        with open('training_history.pkl', 'wb') as f:
            pickle.dump(history.history, f)
        print("Training history saved as: training_history.pkl")
        
    except Exception as e:
        print(f"Training failed: {str(e)}")


if __name__ == "__main__":
    main()
