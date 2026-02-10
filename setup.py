"""
Setup script for SD19 Handwritten Character Recognition System
"""
from setuptools import setup, find_packages
import os

# Read README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

# Read version
version = {}
with open("src/__init__.py", "r", encoding="utf-8") as fh:
    exec(fh.read(), version)

setup(
    name="sd19-character-recognition",
    version=version["__version__"],
    author="Sandalu Umayanga, Milinda Perera, Sampath K.G.H., Nadeeka Dissanayake",
    author_email="e20284@eng.pdn.ac.lk, e20286@eng.pdn.ac.lk, e19490@eng.pdn.ac.lk, e20078@eng.pdn.ac.lk",
    description=version["__description__"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cepdnaclk/e20-co542-handwritten-character-recognition",
    project_urls={
        "Bug Tracker": "https://github.com/cepdnaclk/e20-co542-handwritten-character-recognition/issues",
        "Documentation": "https://cepdnaclk.github.io/e20-co542-handwritten-character-recognition/",
        "Source Code": "https://github.com/cepdnaclk/e20-co542-handwritten-character-recognition",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.900",
            "pre-commit>=2.0",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=1.0",
            "myst-parser>=0.15",
        ],
        "gpu": [
            "torch[cuda]",
            "tensorflow[gpu]",
        ],
    },
    entry_points={
        "console_scripts": [
            "sd19-gui=src.gui.application:main",
            "sd19-train=main:main",
            "sd19-predict=main:predict_image",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.yml", "*.yaml"],
    },
    keywords=[
        "handwriting recognition",
        "character recognition",
        "deep learning",
        "computer vision",
        "neural networks",
        "pytorch",
        "tensorflow",
        "OCR",
        "machine learning",
        "NIST SD19",
    ],
    zip_safe=False,
)
