# Project Structure

This document explains the organization and structure of the SD19 Handwritten Character Recognition project.

## Root Directory Structure

```
e20-co542-handwritten-character-recognition/
├── src/                    # Source code
├── scripts/                # Training and utility scripts
├── tests/                  # Unit tests
├── data/                   # Dataset directory
├── saved_models/           # Trained model files
├── docs/                   # Documentation
├── main.py                 # Main entry point
├── setup.py                # Package setup
├── requirements.txt        # Python dependencies
├── README.md              # Project overview
├── LICENSE                # License information
├── CONTRIBUTING.md        # Contribution guidelines
├── CHANGELOG.md           # Version history
└── .gitignore            # Git ignore rules
```

## Source Code (`src/`)

### Core Modules

```
src/
├── __init__.py            # Package initialization
├── models/                # Model implementations
│   ├── __init__.py
│   ├── pytorch_model.py   # PyTorch CNN implementation
│   ├── keras_model.py     # TensorFlow/Keras implementation
│   └── README.md          # Model documentation
├── utils/                 # Utility functions
│   ├── __init__.py
│   ├── preprocessing.py   # Image preprocessing utilities
│   └── prediction.py      # Model prediction utilities
└── gui/                   # GUI application
    ├── __init__.py
    └── application.py     # Main GUI application
```

### Module Responsibilities

#### `src/models/`
- **Model Architecture**: Defines CNN architectures for both PyTorch and TensorFlow
- **Model Loading**: Functions to load pre-trained models
- **Framework Abstraction**: Unified interface for different frameworks

#### `src/utils/`
- **Preprocessing**: Image preprocessing and data augmentation
- **Prediction**: Unified prediction interface for both frameworks
- **Validation**: Data validation and utility functions

#### `src/gui/`
- **User Interface**: Interactive GUI for drawing and prediction
- **File Handling**: Image upload and processing
- **Model Integration**: Seamless integration with both model types

## Scripts (`scripts/`)

```
scripts/
├── train_pytorch.py       # PyTorch model training
└── train_keras.py         # TensorFlow/Keras model training
```

### Training Scripts
- **Data Loading**: Custom dataset classes and data loaders
- **Training Loop**: Complete training pipeline with validation
- **Model Saving**: Checkpoint and final model persistence
- **Logging**: Training progress and metrics logging

## Tests (`tests/`)

```
tests/
├── test_preprocessing.py  # Unit tests for preprocessing
├── test_models.py        # Model architecture tests
├── test_prediction.py    # Prediction functionality tests
└── conftest.py          # Test configuration
```

### Testing Strategy
- **Unit Tests**: Individual function and class testing
- **Integration Tests**: Module interaction testing
- **End-to-End Tests**: Complete workflow testing
- **Performance Tests**: Model performance benchmarks

## Data (`data/`)

```
data/
├── README.md             # Dataset documentation
└── by_merge/            # SD19 dataset (when downloaded)
    ├── 0/               # Digit '0' images
    ├── 1/               # Digit '1' images
    ├── ...
    ├── A/               # Letter 'A' images
    ├── B/               # Letter 'B' images
    └── ...
```

### Data Organization
- **Class-based Structure**: Each character class in separate directory
- **Image Format**: Grayscale PNG/JPEG files
- **Naming Convention**: Descriptive filenames for traceability

## Documentation (`docs/`)

```
docs/
├── README.md             # Project documentation homepage
├── INSTALLATION.md       # Installation instructions
├── API.md               # API documentation
├── _config.yml          # Jekyll configuration
├── Gemfile              # Ruby dependencies
├── data/
│   └── index.json       # Data configuration
└── images/
    └── sample.png       # Sample images
```

### Documentation Types
- **User Documentation**: Installation, usage guides
- **Developer Documentation**: API reference, contributing guidelines
- **Technical Documentation**: Architecture, design decisions
- **Examples**: Code examples and tutorials

## Configuration Files

### `requirements.txt`
- Lists all Python dependencies
- Includes version constraints for reproducibility
- Organized by functionality (core, ML, GUI, dev)

### `setup.py`
- Package configuration for installation
- Entry points for command-line tools
- Metadata and classification

### `.gitignore`
- Excludes temporary files and directories
- Protects sensitive information
- Maintains clean repository

## Design Principles

### Modularity
- **Separation of Concerns**: Each module has a specific responsibility
- **Loose Coupling**: Modules interact through well-defined interfaces
- **High Cohesion**: Related functionality grouped together

### Extensibility
- **Plugin Architecture**: Easy to add new model implementations
- **Framework Agnostic**: Support for multiple ML frameworks
- **Configurable**: Parameters and settings externalized

### Maintainability
- **Clear Naming**: Descriptive names for files, functions, and variables
- **Documentation**: Comprehensive docstrings and comments
- **Testing**: Good test coverage for critical functionality

### Usability
- **Simple Interface**: Easy-to-use API and GUI
- **Error Handling**: Graceful error handling and reporting
- **Logging**: Informative logging for debugging

## Development Workflow

### Adding New Features

1. **Create Feature Branch**: `git checkout -b feature/new-feature`
2. **Implement Feature**: Add code in appropriate module
3. **Add Tests**: Create unit tests for new functionality
4. **Update Documentation**: Update relevant documentation files
5. **Submit Pull Request**: Follow contribution guidelines

### Code Organization Guidelines

#### File Naming
- Use lowercase with underscores: `file_name.py`
- Be descriptive but concise
- Group related files in directories

#### Import Organization
- Standard library imports first
- Third-party imports second
- Local imports last
- Use absolute imports when possible

#### Function and Class Organization
- Group related functions in classes when appropriate
- Use inheritance sparingly and purposefully
- Prefer composition over inheritance

### Testing Strategy

#### Test File Organization
- Mirror the source code structure
- Use descriptive test names
- Group related tests in classes

#### Test Coverage
- Aim for >80% code coverage
- Focus on critical paths
- Include edge cases and error conditions

## Deployment Considerations

### Package Distribution
- Use `setup.py` for package installation
- Include all necessary files in package
- Specify appropriate dependencies

### Environment Setup
- Provide clear installation instructions
- Support virtual environments
- Handle different operating systems

### Model Distribution
- Separate model files from code
- Provide pre-trained models when possible
- Document model versions and performance

This structure promotes maintainability, extensibility, and ease of use while following Python best practices and software engineering principles.
