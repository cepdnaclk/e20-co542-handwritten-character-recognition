# Changelog

All notable changes to the SD19 Handwritten Character Recognition project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial project structure and organization
- Comprehensive documentation suite
- Contributing guidelines and development setup

### Changed
- Reorganized codebase into modular structure
- Improved code documentation and type hints

### Fixed
- Code organization and dependency management

## [1.0.0] - 2025-01-31

### Added
- Initial implementation of SD19 handwritten character recognition system
- PyTorch CNN model for character classification
- TensorFlow/Keras alternative implementation
- Interactive GUI application using Tkinter
- Support for 47 character classes (digits, uppercase, lowercase)
- Image preprocessing and augmentation pipeline
- Model training and evaluation scripts
- Batch prediction capabilities
- File upload and canvas drawing interfaces

### Features
- **Dual Framework Support**: Both PyTorch and TensorFlow implementations
- **Interactive GUI**: User-friendly drawing and prediction interface
- **High Accuracy**: Achieves >90% validation accuracy on SD19 dataset
- **Robust Preprocessing**: Advanced image preprocessing with augmentation
- **Model Persistence**: Save and load trained models
- **Batch Processing**: Efficient batch prediction for multiple images

### Technical Specifications
- **Input Size**: 128×128 pixel grayscale images
- **Architecture**: CNN with 3 convolutional blocks + 2 dense layers
- **Training**: Adam optimizer with learning rate scheduling
- **Data Augmentation**: Rotation, shifting, and zoom transformations
- **Regularization**: Dropout and batch normalization

### Performance
- **Training Accuracy**: ~95%
- **Validation Accuracy**: ~92%
- **Inference Time**: <100ms per image on CPU
- **Model Size**: ~15MB

### Components

#### Core Models
- `neural_model.py`: TensorFlow/Keras CNN implementation
- `neural_model_with_pytorch.py`: PyTorch CNN implementation
- `application.py`: Main GUI application

#### Utilities
- `loading_and_preprocessing.py`: Data loading and preprocessing
- `file_uploader_and_predict.py`: File handling and prediction
- `accuracy_checking.py`: Model evaluation utilities
- `label_checking.py`: Label validation functions

#### Assets
- `sd19_model.h5`: Pre-trained Keras model
- `sd19_model.pth`: Pre-trained PyTorch model
- `requirements.txt`: Python dependencies

### Known Issues
- GUI may not display properly on some Linux distributions without X11
- Large batch predictions may cause memory issues on systems with <8GB RAM
- Model loading time can be slow on systems without SSD storage

### Dependencies
- TensorFlow 2.x
- PyTorch 1.x
- NumPy
- Pillow (PIL)
- Tkinter
- Matplotlib
- Additional packages listed in requirements.txt

## Project Milestones

### Milestone 1: Core Implementation ✅
- [x] Basic CNN model implementation
- [x] Data preprocessing pipeline
- [x] Training scripts
- [x] Basic GUI interface
- [x] Model evaluation

### Milestone 2: Code Organization (Current)
- [x] Modular project structure
- [x] Comprehensive documentation
- [x] API documentation
- [x] Installation guides
- [x] Contributing guidelines
- [x] Unit testing framework

### Milestone 3: Enhanced Features (Planned)
- [ ] Web-based interface
- [ ] Real-time video recognition
- [ ] Mobile app prototype
- [ ] Model optimization and quantization
- [ ] Additional dataset support

### Milestone 4: Production Ready (Future)
- [ ] Docker containerization
- [ ] CI/CD pipeline
- [ ] Performance benchmarking
- [ ] Security audit
- [ ] Production deployment guide

## Version History

### Development Phases

#### Phase 1: Research and Prototyping (Weeks 1-4)
- Literature review and dataset analysis
- Initial model architecture design
- Proof of concept implementation
- Baseline performance evaluation

#### Phase 2: Implementation (Weeks 5-8)
- Full model implementation in both frameworks
- GUI application development
- Training pipeline optimization
- Model evaluation and validation

#### Phase 3: Integration and Testing (Weeks 9-10)
- Component integration
- End-to-end testing
- Performance optimization
- Bug fixes and improvements

#### Phase 4: Documentation and Organization (Weeks 11-12)
- Code reorganization
- Comprehensive documentation
- User guides and API documentation
- Project finalization

## Breaking Changes

### From Unorganized to v1.0.0
- **File Structure**: Complete reorganization of project structure
- **Import Paths**: All imports now use the new modular structure
- **API Changes**: Unified prediction interface through ModelPredictor class
- **Configuration**: New configuration system for model parameters

### Migration Guide

#### For Users
1. Re-clone the repository or pull latest changes
2. Reinstall dependencies: `pip install -r requirements.txt`
3. Update any custom scripts to use new import paths
4. Use new GUI application: `python src/gui/application.py`

#### For Developers
1. Update development environment setup
2. Use new project structure for contributions
3. Follow new coding standards and documentation requirements
4. Use updated testing framework

## Contributors

### Core Team
- **E/20/284** - Sandalu Umayanga - Project Lead & ML Engineer
- **E/20/286** - Milinda Perera - Software Engineer & GUI Developer  
- **E/19/490** - Sampath K.G.H. - ML Engineer & Documentation
- **E/20/078** - Nadeeka Dissanayake - Data Engineer & Testing

### Acknowledgments
- University of Peradeniya - Department of Computer Engineering
- NIST for providing the SD19 dataset
- Open source community for tools and libraries

## Future Roadmap

### Short Term (Next 3 months)
- [ ] Performance optimizations
- [ ] Additional model architectures (ResNet, Vision Transformer)
- [ ] Web interface development
- [ ] Mobile app prototype

### Medium Term (3-6 months)
- [ ] Real-time video recognition
- [ ] Multi-language support
- [ ] Cloud deployment options
- [ ] Enterprise features

### Long Term (6+ months)
- [ ] Advanced AI features (style transfer, generation)
- [ ] Integration with educational platforms
- [ ] Commercial applications
- [ ] Research publications



For more information about releases and changes, see the [GitHub Releases](https://github.com/cepdnaclk/e20-co542-handwritten-character-recognition/releases) page.
