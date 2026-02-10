# Installation Guide

## System Requirements

### Minimum Requirements
- **Operating System**: Windows 10, macOS 10.14, Ubuntu 18.04 or newer
- **Python**: 3.7 or higher
- **RAM**: 4GB
- **Storage**: 2GB free space
- **Processor**: Multi-core CPU

### Recommended Requirements
- **Operating System**: Windows 11, macOS 12, Ubuntu 20.04 or newer
- **Python**: 3.8 or higher
- **RAM**: 8GB or more
- **Storage**: 5GB free space (for dataset)
- **Processor**: Multi-core CPU with AVX support
- **Graphics**: NVIDIA GPU with CUDA support (optional but recommended)

## Installation Methods

### Method 1: Quick Start (Recommended)

1. **Clone the repository**
   ```bash
   git clone https://github.com/cepdnaclk/e20-co542-handwritten-character-recognition.git
   cd e20-co542-handwritten-character-recognition
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify installation**
   ```bash
   python -c "import torch, tensorflow; print('Installation successful!')"
   ```

### Method 2: Development Setup

For contributors and developers who want to modify the code:

1. **Fork and clone**
   ```bash
   git clone https://github.com/YOUR_USERNAME/e20-co542-handwritten-character-recognition.git
   cd e20-co542-handwritten-character-recognition
   ```

2. **Install development dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # If available
   ```

3. **Install in development mode**
   ```bash
   pip install -e .
   ```

4. **Set up pre-commit hooks** (optional)
   ```bash
   pre-commit install
   ```

## Platform-Specific Instructions

### Windows

1. **Install Python**
   - Download from [python.org](https://www.python.org/downloads/)
   - During installation, check "Add Python to PATH"

2. **Install Git**
   - Download from [git-scm.com](https://git-scm.com/download/win)

3. **Install Visual C++ Build Tools** (if needed)
   - Download from [Microsoft](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

4. **CUDA Setup** (for GPU support)
   - Install [NVIDIA CUDA Toolkit](https://developer.nvidia.com/cuda-downloads)
   - Install [cuDNN](https://developer.nvidia.com/cudnn)

### macOS

1. **Install Homebrew**
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Python and Git**
   ```bash
   brew install python git
   ```

3. **Install Xcode Command Line Tools**
   ```bash
   xcode-select --install
   ```

### Linux (Ubuntu/Debian)

1. **Update package list**
   ```bash
   sudo apt update
   ```

2. **Install Python and dependencies**
   ```bash
   sudo apt install python3 python3-pip python3-venv git
   ```

3. **Install system dependencies**
   ```bash
   sudo apt install python3-tk  # For GUI support
   sudo apt install build-essential  # For compiling packages
   ```

4. **CUDA Setup** (for GPU support)
   ```bash
   # Add NVIDIA package repository
   wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
   sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
   wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda-repo-ubuntu2004-11-8-local_11.8.0-520.61.05-1_amd64.deb
   sudo dpkg -i cuda-repo-ubuntu2004-11-8-local_11.8.0-520.61.05-1_amd64.deb
   sudo cp /var/cuda-repo-ubuntu2004-11-8-local/cuda-*-keyring.gpg /usr/share/keyrings/
   sudo apt-get update
   sudo apt-get -y install cuda
   ```

### Linux (CentOS/RHEL)

1. **Install EPEL repository**
   ```bash
   sudo yum install epel-release
   ```

2. **Install Python and Git**
   ```bash
   sudo yum install python3 python3-pip git
   ```

3. **Install development tools**
   ```bash
   sudo yum groupinstall "Development Tools"
   ```

## Dataset Setup

### Download SD19 Dataset

1. **Visit NIST website**
   - Go to [NIST Special Database 19](https://www.nist.gov/srd/nist-special-database-19)

2. **Download the dataset**
   - Download "by_merge" directory
   - File size: ~3GB

3. **Extract and organize**
   ```bash
   # Create data directory
   mkdir -p data
   
   # Extract dataset (example)
   unzip sd19_by_merge.zip -d data/
   
   # Verify structure
   ls data/by_merge/
   # Should show directories: 0, 1, 2, ..., 9, A, B, ..., Z, a, b, ...
   ```

### Alternative: Sample Dataset

For quick testing, you can use a smaller sample:

```bash
# Download sample data (if provided)
wget https://example.com/sd19_sample.zip
unzip sd19_sample.zip -d data/
```

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```bash
# Data paths
DATA_DIR=data/by_merge
MODEL_DIR=saved_models

# Training configuration
BATCH_SIZE=32
LEARNING_RATE=0.001
EPOCHS=50

# GPU configuration
CUDA_VISIBLE_DEVICES=0
```

### Model Configuration

Edit configuration files if needed:

```python
# config.py (create if needed)
CONFIG = {
    'model': {
        'input_size': (128, 128),
        'num_classes': 47,
        'dropout_rate': 0.5
    },
    'training': {
        'batch_size': 32,
        'learning_rate': 0.001,
        'epochs': 50
    }
}
```

## Verification

### Test Installation

1. **Run basic test**
   ```bash
   python -c "
   from src.models.pytorch_model import SD19Model
   from src.models.keras_model import create_sd19_model
   print('Models imported successfully!')
   "
   ```

2. **Test GUI (if X11 available)**
   ```bash
   python src/gui/application.py
   ```

3. **Run unit tests**
   ```bash
   python -m pytest tests/ -v
   ```

### Troubleshooting

#### Common Issues

1. **ModuleNotFoundError**
   ```bash
   # Solution: Install missing packages
   pip install [missing_package]
   ```

2. **CUDA not available**
   ```bash
   # Check CUDA installation
   python -c "import torch; print(torch.cuda.is_available())"
   
   # If False, install CUDA-compatible PyTorch
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   ```

3. **Permission denied (Linux/macOS)**
   ```bash
   # Solution: Use virtual environment or add --user flag
   pip install --user -r requirements.txt
   ```

4. **Tkinter not found**
   ```bash
   # Ubuntu/Debian
   sudo apt install python3-tk
   
   # CentOS/RHEL
   sudo yum install tkinter
   
   # macOS
   brew install python-tk
   ```

5. **Out of memory during training**
   ```bash
   # Reduce batch size in training scripts
   # Edit scripts/train_pytorch.py or scripts/train_keras.py
   BATCH_SIZE = 16  # Instead of 32
   ```

#### Getting Help

1. **Check logs**
   ```bash
   # Enable verbose logging
   export PYTHONPATH=$PYTHONPATH:$(pwd)
   python -v src/gui/application.py
   ```

2. **Create issue**
   - Visit [GitHub Issues](https://github.com/cepdnaclk/e20-co542-handwritten-character-recognition/issues)
   - Provide system information and error messages

3. **Community support**
   - Check existing issues and discussions
   - Provide minimal reproducible example

## Next Steps

After successful installation:

1. **Download pre-trained models** (if available)
2. **Run the GUI application**
3. **Try training your own model**
4. **Explore the API documentation**

## Updating

To update to the latest version:

```bash
# Pull latest changes
git pull origin main

# Update dependencies
pip install -r requirements.txt --upgrade

# Check for breaking changes in CHANGELOG.md
```

## Uninstallation

To completely remove the project:

```bash
# Deactivate virtual environment
deactivate

# Remove project directory
rm -rf e20-co542-handwritten-character-recognition

# Remove virtual environment
rm -rf venv
```
