# SD19 Handwritten Character Recognition System

A deep learning-based system for recognizing handwritten characters using Convolutional Neural Networks (CNNs). This project implements both PyTorch and TensorFlow/Keras models trained on the SD19 dataset to classify 47 different character classes including digits (0-9), uppercase letters (A-Z), and lowercase letters (a-z).

## � Team

This project was developed by students from the Department of Computer Engineering, University of Peradeniya as part of the CO542 Neural Networks and Fuzzy Systems course.

**Team Members:**
- **E/20/284** - Sandalu Umayanga ([e20284@eng.pdn.ac.lk](mailto:e20284@eng.pdn.ac.lk))
- **E/20/286** - Milinda Perera ([e20286@eng.pdn.ac.lk](mailto:e20286@eng.pdn.ac.lk))
- **E/19/490** - Sampath K.G.H. ([e19490@eng.pdn.ac.lk](mailto:e19490@eng.pdn.ac.lk))
- **E/20/078** - Nadeeka Dissanayake ([e20078@eng.pdn.ac.lk](mailto:e20078@eng.pdn.ac.lk))

## �🚀 Features

- **Dual Framework Support**: Both PyTorch and TensorFlow/Keras implementations
- **Interactive GUI Application**: User-friendly interface for drawing and predicting characters
- **High Accuracy**: Achieves competitive accuracy on SD19 dataset
- **Robust Preprocessing**: Advanced image preprocessing pipeline
- **Model Persistence**: Save and load trained models
- **Comprehensive Testing**: Unit tests for critical components
- **Well-documented Code**: Clear documentation and examples

## 📁 Project Structure

```
├── src/                          # Source code
│   ├── models/                   # Model architectures
│   │   ├── pytorch_model.py      # PyTorch CNN implementation
│   │   └── keras_model.py        # TensorFlow/Keras implementation
│   ├── utils/                    # Utility functions
│   │   ├── preprocessing.py      # Image preprocessing utilities
│   │   └── prediction.py         # Model prediction utilities
│   └── gui/                      # GUI application
│       └── application.py        # Main GUI application
├── scripts/                      # Training scripts
│   ├── train_pytorch.py          # PyTorch training script
│   └── train_keras.py            # TensorFlow training script
├── tests/                        # Unit tests
│   └── test_preprocessing.py     # Preprocessing tests
├── data/                         # Data directory (add your dataset here)
├── saved_models/                 # Trained model files
├── docs/                         # Documentation
└── requirements.txt              # Python dependencies
```

## 🛠 Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/cepdnaclk/e20-co542-handwritten-character-recognition.git
   cd e20-co542-handwritten-character-recognition
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Dataset Setup

1. Download the SD19 dataset from [NIST Special Database 19](https://www.nist.gov/srd/nist-special-database-19)
2. Extract the dataset to the `data/` directory
3. Ensure the data structure follows the format:
   ```
   data/
   └── by_merge/
       ├── 0/
       ├── 1/
       ├── A/
       ├── B/
       └── ... (47 character classes total)
   ```

## 🎯 Usage

### Training Models

#### PyTorch Model
```bash
python scripts/train_pytorch.py
```

#### TensorFlow/Keras Model
```bash
python scripts/train_keras.py
```

### Running the GUI Application

```bash
python src/gui/application.py
```

The GUI provides:
- **Drawing Canvas**: Draw characters with your mouse
- **File Upload**: Upload image files for prediction
- **Model Loading**: Load different trained models
- **Real-time Prediction**: Get instant character predictions

### Using Models Programmatically

#### PyTorch Example
```python
from src.models.pytorch_model import load_model
from src.utils.prediction import ModelPredictor

# Load model
model = load_model('saved_models/sd19_model.pth')
predictor = ModelPredictor(model, 'pytorch')

# Predict from image file
predicted_class, confidence = predictor.predict_image('path/to/image.png')
print(f"Predicted: {predicted_class} (Confidence: {confidence:.2%})")
```

#### TensorFlow Example
```python
from src.models.keras_model import load_keras_model
from src.utils.prediction import ModelPredictor

# Load model
model = load_keras_model('saved_models/sd19_model.h5')
predictor = ModelPredictor(model, 'tensorflow')

# Predict from image file
predicted_class, confidence = predictor.predict_image('path/to/image.png')
print(f"Predicted: {predicted_class} (Confidence: {confidence:.2%})")
```

## 🧪 Testing

Run the test suite:
```bash
python -m pytest tests/ -v
```

Or run specific tests:
```bash
python tests/test_preprocessing.py
```

## 📊 Model Architecture

### CNN Architecture
Both PyTorch and TensorFlow models use similar architectures:

1. **Convolutional Layers**:
   - Conv2D (32 filters, 3x3 kernel) + ReLU + BatchNorm + MaxPool
   - Conv2D (64 filters, 3x3 kernel) + ReLU + BatchNorm + MaxPool
   - Conv2D (128 filters, 3x3 kernel) + ReLU + BatchNorm + MaxPool

2. **Classification Layers**:
   - Flatten
   - Dense (512 units) + ReLU + Dropout(0.5)
   - Dense (47 units, softmax activation)

### Input Specifications
- **Image Size**: 128x128 pixels
- **Color**: Grayscale (1 channel)
- **Normalization**: Pixel values normalized to [0, 1]

### Character Classes (47 total)
- **Digits**: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
- **Uppercase**: A, B, C.c, D, E, F, G, H, I.i, J.j, K.k, L.l, M.m, N, O.o, P.p, Q, R, S.s, T, U.u, V.v, W.w, X.x, Y.y, Z.z
- **Lowercase**: a, b, d, e, f, g, h, n, q, r, t

## 📈 Performance

The models achieve competitive performance on the SD19 dataset:
- **Training Accuracy**: ~95%+
- **Validation Accuracy**: ~92%+
- **Inference Time**: <100ms per image on CPU

## 🔧 Configuration

### Training Parameters
- **Batch Size**: 32
- **Learning Rate**: 0.001
- **Epochs**: 50
- **Optimizer**: Adam
- **Loss Function**: Categorical Crossentropy

### Data Augmentation
- Rotation: ±10 degrees
- Width/Height Shift: ±10%
- Zoom: ±10%

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📋 Dependencies

### Core Libraries
- **TensorFlow**: 2.x for Keras implementation
- **PyTorch**: 1.x for PyTorch implementation
- **NumPy**: Numerical computations
- **Pillow**: Image processing
- **Tkinter**: GUI framework

### Development
- **pytest**: Testing framework
- **matplotlib**: Visualization
- **scikit-learn**: Metrics and utilities

See `requirements.txt` for complete list with versions.

## 🐛 Troubleshooting

### Common Issues

1. **"Module not found" errors**
   - Ensure you're in the project root directory
   - Check if virtual environment is activated
   - Verify all dependencies are installed

2. **CUDA out of memory (PyTorch)**
   - Reduce batch size in training scripts
   - Use CPU instead: set `device='cpu'`

3. **GUI not displaying**
   - Install tkinter: `sudo apt-get install python3-tk` (Ubuntu/Debian)
   - Ensure X11 forwarding if using SSH

4. **Low prediction accuracy**
   - Ensure input images are preprocessed correctly
   - Check that model file is not corrupted
   - Verify image orientation (black text on white background)


## 🙏 Acknowledgments

- **NIST** for providing the SD19 dataset
- **TensorFlow** and **PyTorch** communities for excellent documentation
- **University of Peradeniya** - Department of Computer Engineering

## 📞 Contact

For questions, suggestions, or collaboration opportunities:

- **Repository**: [GitHub](https://github.com/cepdnaclk/e20-co542-handwritten-character-recognition)
- **Issues**: [GitHub Issues](https://github.com/cepdnaclk/e20-co542-handwritten-character-recognition/issues)

---

## 🔮 Future Enhancements

- [ ] Real-time video character recognition
- [ ] Mobile app implementation
- [ ] Support for additional datasets (EMNIST, etc.)
- [ ] Model quantization for edge deployment
- [ ] Web-based interface
- [ ] Multi-character sequence recognition
