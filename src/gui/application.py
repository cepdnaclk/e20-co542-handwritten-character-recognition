"""
GUI Application for Handwritten Character Recognition
"""
import tkinter as tk
from tkinter import Canvas, Button, Toplevel, Label, filedialog, messagebox
from PIL import Image, ImageDraw, ImageOps
import numpy as np
import os
import sys

# Add parent directory to path to import from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils.prediction import ModelPredictor
from src.utils.preprocessing import preprocess_canvas_image


class HandwritingApp:
    """
    GUI application for handwritten character recognition.
    """
    
    def __init__(self, master, model_path=None, model_type='pytorch'):
        """
        Initialize the GUI application.
        
        Args:
            master: Tkinter root window
            model_path (str): Path to the trained model
            model_type (str): Type of model ('pytorch' or 'tensorflow')
        """
        self.master = master
        master.title("SD19 Handwritten Character Recognition")
        master.geometry("800x600")
        
        # Initialize model
        self.predictor = None
        
        # Initialize drawing variables
        self.old_x = None
        self.old_y = None
        
        # Create GUI components
        self.create_widgets()
        
        # Auto-load model after widgets are created
        if model_path:
            self.load_model(model_path, model_type)
        else:
            # Try to auto-load a default model
            self.auto_load_default_model()
    
    def auto_load_default_model(self):
        """Automatically load a default model if available."""
        keras_model = 'saved_models/sd19_model.h5'
        pytorch_model = 'saved_models/sd19_model.pth'
        
        # Try Keras model first (usually more stable)
        if os.path.exists(keras_model):
            try:
                self.load_model(keras_model, 'tensorflow')
                print(f"Auto-loaded Keras model: {keras_model}")
                return
            except Exception as e:
                print(f"Failed to auto-load Keras model: {e}")
        
        # Try PyTorch model as fallback
        if os.path.exists(pytorch_model):
            try:
                self.load_model(pytorch_model, 'pytorch')
                print(f"Auto-loaded PyTorch model: {pytorch_model}")
                return
            except Exception as e:
                print(f"Failed to auto-load PyTorch model: {e}")
        
        print("No default model found. Please load a model manually.")
    
    def create_widgets(self):
        """Create and layout GUI widgets."""
        # Title
        title_label = Label(self.master, text="Handwritten Character Recognition", 
                          font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # Instructions
        instructions = Label(self.master, 
                           text="Draw a character in the canvas below or upload an image file",
                           font=("Arial", 12))
        instructions.pack(pady=5)
        
        # Button frame
        button_frame = tk.Frame(self.master)
        button_frame.pack(pady=10)
        
        # Load model button
        load_model_btn = Button(button_frame, text="Load Model", 
                              command=self.load_model_dialog,
                              bg="#4CAF50", fg="white", font=("Arial", 10))
        load_model_btn.pack(side=tk.LEFT, padx=5)
        
        # Upload image button
        upload_btn = Button(button_frame, text="Upload Image", 
                          command=self.upload_image,
                          bg="#2196F3", fg="white", font=("Arial", 10))
        upload_btn.pack(side=tk.LEFT, padx=5)
        
        # Clear canvas button
        clear_btn = Button(button_frame, text="Clear Canvas", 
                         command=self.clear_canvas,
                         bg="#FF9800", fg="white", font=("Arial", 10))
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Predict button
        predict_btn = Button(button_frame, text="Predict", 
                           command=self.predict_character,
                           bg="#9C27B0", fg="white", font=("Arial", 10))
        predict_btn.pack(side=tk.LEFT, padx=5)
        
        # Canvas for drawing
        self.canvas = Canvas(self.master, width=400, height=400, 
                           bg='white', cursor='cross')
        self.canvas.pack(pady=20)
        
        # Bind mouse events
        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonPress-1>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)
        
        # Result display
        self.result_frame = tk.Frame(self.master)
        self.result_frame.pack(pady=10)
        
        self.result_label = Label(self.result_frame, text="Prediction will appear here", 
                                font=("Arial", 14, "bold"))
        self.result_label.pack()
        
        self.confidence_label = Label(self.result_frame, text="", 
                                    font=("Arial", 12))
        self.confidence_label.pack()
        
        # Status bar
        self.status_label = Label(self.master, text="Ready - Load a model to start predicting", 
                                relief=tk.SUNKEN, anchor=tk.W)
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)
    
    def load_model_dialog(self):
        """Open dialog to load a model file."""
        file_path = filedialog.askopenfilename(
            title="Select Model File",
            filetypes=[
                ("PyTorch Models", "*.pth"),
                ("Keras Models", "*.h5"),
                ("All Files", "*.*")
            ]
        )
        
        if file_path:
            # Determine model type from extension
            if file_path.endswith('.pth'):
                model_type = 'pytorch'
            elif file_path.endswith('.h5'):
                model_type = 'tensorflow'
            else:
                messagebox.showerror("Error", "Unsupported model format")
                return
            
            self.load_model(file_path, model_type)
    
    def load_model(self, model_path, model_type):
        """Load a trained model."""
        try:
            if model_type == 'pytorch':
                from src.models.pytorch_model import load_model
                model = load_model(model_path)
            else:
                from src.models.keras_model import load_keras_model
                model = load_keras_model(model_path)
            
            self.predictor = ModelPredictor(model, model_type)
            self.status_label.config(text=f"Model loaded: {os.path.basename(model_path)}")
            messagebox.showinfo("Success", "Model loaded successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load model: {str(e)}")
            self.status_label.config(text="Failed to load model")
    
    def paint(self, event):
        """Handle drawing on canvas."""
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                                  width=8, fill='black', capstyle=tk.ROUND, smooth=tk.TRUE)
        self.old_x = event.x
        self.old_y = event.y
    
    def reset(self, event):
        """Reset drawing coordinates."""
        self.old_x, self.old_y = None, None
    
    def clear_canvas(self):
        """Clear the drawing canvas."""
        self.canvas.delete("all")
        self.result_label.config(text="Prediction will appear here")
        self.confidence_label.config(text="")
    
    def upload_image(self):
        """Upload and predict an image file."""
        if not self.predictor:
            messagebox.showerror("Error", "Please load a model first")
            return
        
        file_path = filedialog.askopenfilename(
            title="Select Image File",
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.bmp *.tiff"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            try:
                predicted_class, confidence = self.predictor.predict_image(file_path)
                self.display_result(predicted_class, confidence)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to predict image: {str(e)}")
    
    def predict_character(self):
        """Predict the character drawn on canvas."""
        if not self.predictor:
            messagebox.showwarning("Warning", "Please load a model first")
            return
        
        try:
            # Create image from canvas drawing data
            canvas_image = self.canvas_to_image()
            
            if canvas_image is None:
                messagebox.showwarning("Warning", "No drawing detected. Please draw a character first.")
                return
            
            # Predict
            predicted_class, confidence = self.predictor.predict_pil_image(canvas_image)
            self.display_result(predicted_class, confidence)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to predict character: {str(e)}")
    
    def canvas_to_image(self):
        """Convert canvas drawing to PIL Image."""
        try:
            # Get canvas dimensions
            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()
            
            # Create a white image
            image = Image.new('RGB', (canvas_width, canvas_height), 'white')
            draw = ImageDraw.Draw(image)
            
            # Get all canvas items (lines drawn)
            items = self.canvas.find_all()
            
            if not items:
                return None
            
            # Draw each line on the image
            drawn_something = False
            for i, item in enumerate(items):
                # Get item type and coordinates
                item_type = self.canvas.type(item)
                
                if item_type == 'line':
                    coords = self.canvas.coords(item)
                    
                    if len(coords) >= 4:
                        # Get line width and color from canvas item
                        try:
                            width = int(self.canvas.itemcget(item, 'width'))
                        except:
                            width = 8  # Default width
                        
                        # Each tkinter line has exactly 4 coordinates: x1, y1, x2, y2
                        x1, y1, x2, y2 = coords[0], coords[1], coords[2], coords[3]
                        draw.line([(x1, y1), (x2, y2)], fill='black', width=width)
                        drawn_something = True
            
            if not drawn_something:
                print("No lines were drawn on the image!")
                return None
            
            # Convert to grayscale and resize
            image = image.convert('L')
            
            # Debug: Check if image has any black pixels
            import numpy as np
            img_array = np.array(image)
            min_pixel = img_array.min()
            mean_pixel = img_array.mean()
            print(f"Canvas image stats - Min: {min_pixel}, Mean: {mean_pixel:.1f}")
            
            # If image is mostly white, there might be no drawing
            if mean_pixel > 250:
                print("Warning: Canvas appears to be mostly empty")
            
            image = image.resize((128, 128), Image.LANCZOS)
            
            return image
            
        except Exception as e:
            print(f"Error converting canvas to image: {e}")
            import traceback
            traceback.print_exc()
            return None
    
    def display_result(self, predicted_class, confidence):
        """Display prediction results."""
        self.result_label.config(text=f"Predicted: {predicted_class}")
        self.confidence_label.config(text=f"Confidence: {confidence:.2%}")
        self.status_label.config(text=f"Prediction: {predicted_class} ({confidence:.2%})")


def main():
    """Main function to run the GUI application."""
    root = tk.Tk()
    app = HandwritingApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
