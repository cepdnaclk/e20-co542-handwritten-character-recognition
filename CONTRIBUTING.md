# Contributing to SD19 Handwritten Character Recognition

Thank you for your interest in contributing to this project! This document provides guidelines and information for contributors.

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Getting Started](#getting-started)
3. [Development Setup](#development-setup)
4. [Contributing Guidelines](#contributing-guidelines)
5. [Pull Request Process](#pull-request-process)
6. [Coding Standards](#coding-standards)
7. [Testing](#testing)
8. [Documentation](#documentation)
9. [Reporting Issues](#reporting-issues)

## Code of Conduct

### Our Pledge

We pledge to make participation in our project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards

Examples of behavior that contributes to creating a positive environment include:

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

## Getting Started

### Prerequisites

- Python 3.7+
- Git
- Basic understanding of machine learning and deep learning
- Familiarity with PyTorch or TensorFlow

### First Contribution

1. **Find an issue**: Look for issues labeled `good first issue` or `help wanted`
2. **Comment on the issue**: Let others know you're working on it
3. **Fork the repository**: Create your own copy
4. **Create a branch**: Use a descriptive name
5. **Make changes**: Follow coding standards
6. **Test thoroughly**: Ensure your changes work
7. **Submit a pull request**: Include a clear description

## Development Setup

### 1. Fork and Clone

```bash
# Fork the repository on GitHub
# Then clone your fork
git clone https://github.com/YOUR_USERNAME/e20-co542-handwritten-character-recognition.git
cd e20-co542-handwritten-character-recognition
```

### 2. Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install pytest black flake8 mypy pre-commit

# Install pre-commit hooks
pre-commit install
```

### 3. Add Upstream Remote

```bash
git remote add upstream https://github.com/cepdnaclk/e20-co542-handwritten-character-recognition.git
```

### 4. Verify Setup

```bash
# Run tests
python -m pytest tests/

# Check code style
black --check src/
flake8 src/

# Type checking
mypy src/
```

## Contributing Guidelines

### Types of Contributions

We welcome various types of contributions:

1. **Bug Fixes**: Fix existing issues
2. **New Features**: Add new functionality
3. **Documentation**: Improve or add documentation
4. **Tests**: Add or improve test coverage
5. **Performance**: Optimize existing code
6. **Examples**: Add usage examples or tutorials

### Contribution Areas

#### Machine Learning
- Model architecture improvements
- New training strategies
- Hyperparameter optimization
- Data augmentation techniques

#### Software Engineering
- Code refactoring
- Performance optimization
- Error handling improvements
- API design enhancements

#### User Experience
- GUI improvements
- Better error messages
- Documentation updates
- Example applications

#### Testing and Quality
- Unit test additions
- Integration tests
- Performance benchmarks
- Code coverage improvements

## Pull Request Process

### 1. Create a Feature Branch

```bash
# Update your fork
git checkout main
git pull upstream main

# Create feature branch
git checkout -b feature/your-feature-name
```

### 2. Make Changes

- Follow coding standards (see below)
- Write clear, descriptive commit messages
- Keep commits atomic (one logical change per commit)
- Update documentation as needed

### 3. Test Your Changes

```bash
# Run all tests
python -m pytest tests/ -v

# Run specific tests
python -m pytest tests/test_preprocessing.py

# Check code coverage
python -m pytest --cov=src tests/

# Manual testing
python src/gui/application.py
```

### 4. Commit and Push

```bash
# Stage changes
git add .

# Commit with descriptive message
git commit -m "Add feature: description of what you added"

# Push to your fork
git push origin feature/your-feature-name
```

### 5. Create Pull Request

1. Go to your fork on GitHub
2. Click "New Pull Request"
3. Fill out the PR template
4. Link related issues
5. Request review from maintainers

### Pull Request Template

```markdown
## Description
Brief description of changes made.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Other (please describe)

## Testing
- [ ] Existing tests pass
- [ ] New tests added
- [ ] Manual testing completed

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No new warnings introduced

## Related Issues
Fixes #(issue number)
```

## Coding Standards

### Python Style Guide

We follow PEP 8 with some modifications:

- **Line length**: 88 characters (Black default)
- **String quotes**: Double quotes preferred
- **Import order**: isort configuration in `setup.cfg`

### Code Formatting

We use automated tools for consistency:

```bash
# Format code
black src/ tests/

# Sort imports
isort src/ tests/

# Check style
flake8 src/ tests/

# Type checking
mypy src/
```

### Naming Conventions

- **Variables and functions**: `snake_case`
- **Classes**: `PascalCase`
- **Constants**: `UPPER_SNAKE_CASE`
- **Files and modules**: `snake_case`

### Documentation

- Use docstrings for all public functions and classes
- Follow Google docstring format
- Include type hints for function parameters and returns

Example:

```python
def preprocess_image(image_path: str, target_size: Tuple[int, int] = (128, 128)) -> Image.Image:
    """
    Preprocess an image for model prediction.
    
    Args:
        image_path: Path to the image file
        target_size: Target size for the image (width, height)
        
    Returns:
        Preprocessed PIL Image
        
    Raises:
        FileNotFoundError: If image file doesn't exist
        ValueError: If target_size is invalid
    """
```

### Error Handling

- Use specific exception types
- Provide meaningful error messages
- Log errors appropriately
- Handle edge cases gracefully

```python
try:
    image = Image.open(image_path)
except FileNotFoundError:
    raise FileNotFoundError(f"Image file not found: {image_path}")
except Exception as e:
    raise ValueError(f"Failed to load image: {e}")
```

## Testing

### Test Structure

```
tests/
├── test_preprocessing.py      # Unit tests for preprocessing
├── test_models.py            # Model tests
├── test_prediction.py        # Prediction tests
├── test_gui.py              # GUI tests (if applicable)
└── conftest.py              # Test configuration
```

### Writing Tests

1. **Unit tests**: Test individual functions
2. **Integration tests**: Test component interactions
3. **End-to-end tests**: Test complete workflows

Example test:

```python
import pytest
from src.utils.preprocessing import preprocess_image

class TestPreprocessing:
    def test_preprocess_image_success(self):
        """Test successful image preprocessing."""
        # Arrange
        image_path = "tests/fixtures/test_image.png"
        target_size = (128, 128)
        
        # Act
        result = preprocess_image(image_path, target_size)
        
        # Assert
        assert result.size == target_size
        assert result.mode == 'L'
    
    def test_preprocess_image_file_not_found(self):
        """Test preprocessing with non-existent file."""
        with pytest.raises(FileNotFoundError):
            preprocess_image("nonexistent.png")
```

### Running Tests

```bash
# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=src --cov-report=html

# Run specific test file
python -m pytest tests/test_preprocessing.py

# Run with verbose output
python -m pytest -v

# Run tests matching pattern
python -m pytest -k "test_preprocess"
```

## Documentation

### Types of Documentation

1. **Code Documentation**: Docstrings and comments
2. **API Documentation**: Function and class references
3. **User Documentation**: Installation and usage guides
4. **Developer Documentation**: Architecture and contributing guides

### Building Documentation

If using Sphinx:

```bash
# Install documentation dependencies
pip install sphinx sphinx-rtd-theme

# Build documentation
cd docs/
make html

# View documentation
open _build/html/index.html
```

### Documentation Standards

- Write clear, concise documentation
- Include examples where helpful
- Keep documentation up to date with code changes
- Use proper markdown formatting

## Reporting Issues

### Before Reporting

1. **Search existing issues**: Check if already reported
2. **Try latest version**: Ensure you're using the latest code
3. **Minimal reproduction**: Create a simple example that reproduces the issue

### Issue Template

```markdown
## Bug Description
Clear description of what the bug is.

## To Reproduce
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '...'
3. See error

## Expected Behavior
What you expected to happen.

## Screenshots
If applicable, add screenshots.

## Environment
- OS: [e.g., Ubuntu 20.04]
- Python version: [e.g., 3.8.5]
- Package versions: [paste pip freeze output]

## Additional Context
Any other context about the problem.
```

### Feature Requests

Use the feature request template:

```markdown
## Feature Description
Clear description of the feature.

## Motivation
Why is this feature needed?

## Proposed Solution
How should this feature work?

## Alternatives Considered
Other solutions you've considered.

## Additional Context
Any other context or screenshots.
```

## Community

### Communication Channels

- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: General questions and ideas
- **Pull Requests**: Code contributions and reviews

### Getting Help

1. **Check documentation**: Start with README and docs/
2. **Search issues**: Look for similar problems
3. **Ask questions**: Create a discussion or issue
4. **Join the community**: Participate in discussions

### Recognition

Contributors will be acknowledged in:
- CONTRIBUTORS.md file
- Release notes for significant contributions
- GitHub repository contributors list

## Release Process

### Version Numbering

We use [Semantic Versioning](https://semver.org/):
- **MAJOR**: Incompatible API changes
- **MINOR**: New features (backwards compatible)
- **PATCH**: Bug fixes (backwards compatible)

### Release Checklist

1. Update version numbers
2. Update CHANGELOG.md
3. Create release notes
4. Tag release in Git
5. Update documentation
6. Announce release

Thank you for contributing to the SD19 Handwritten Character Recognition project!
