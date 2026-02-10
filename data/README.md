# Data Directory

This directory should contain the SD19 dataset for training and testing the handwritten character recognition models.

## Expected Structure

```
data/
└── by_merge/
    ├── 0/
    │   ├── image1.png
    │   ├── image2.png
    │   └── ...
    ├── 1/
    ├── 2/
    ├── ...
    ├── 9/
    ├── A/
    ├── B/
    ├── ...
    ├── Z/
    ├── a/
    ├── b/
    └── ...
```

## Getting the Dataset

### Option 1: Download from NIST (Recommended)

1. Visit the official NIST SD19 page: https://www.nist.gov/srd/nist-special-database-19
2. Download the "by_merge" dataset
3. Extract the files to this directory

### Option 2: Alternative Sources

The SD19 dataset is also available through various academic and research institutions. Ensure you download the version that includes all 47 character classes.

## Dataset Information

- **Total Images**: ~814,000 character images
- **Character Classes**: 47 (digits 0-9, uppercase A-Z, lowercase a-z variations)
- **Image Format**: Grayscale PNG files
- **Resolution**: Variable (will be normalized to 128×128)
- **Size**: Approximately 3GB

## Character Classes

The dataset includes the following 47 character classes:

### Digits (10 classes)
0, 1, 2, 3, 4, 5, 6, 7, 8, 9

### Uppercase Letters (26 classes)
A, B, C.c, D, E, F, G, H, I.i, J.j, K.k, L.l, M.m, N, O.o, P.p, Q, R, S.s, T, U.u, V.v, W.w, X.x, Y.y, Z.z

### Lowercase Letters (11 classes)
a, b, d, e, f, g, h, n, q, r, t

Note: Some classes like "C.c" represent merged uppercase and lowercase characters that are visually similar.

## Data Validation

After downloading and extracting the dataset, you can validate it using:

```python
from src.utils.preprocessing import validate_data_directory

# Validate the data directory
is_valid = validate_data_directory('data/by_merge')
if is_valid:
    print("Dataset is properly organized!")
else:
    print("Dataset structure is incorrect.")
```

## Sample Data

If you want to test the system without downloading the full dataset, you can create a small sample:

1. Create directories for a few character classes (e.g., `0/`, `1/`, `A/`, `B/`)
2. Add a few images to each directory
3. Ensure images are grayscale and reasonably sized

## Data Preprocessing

The training scripts automatically handle:
- **Resizing**: All images are resized to 128×128 pixels
- **Normalization**: Pixel values are normalized to [0, 1]
- **Augmentation**: Random rotation, shifting, and zooming during training
- **Grayscale Conversion**: Ensures single-channel input

## Privacy and Usage

The SD19 dataset is in the public domain and freely available for research and commercial use. The dataset was created by NIST (National Institute of Standards and Technology) and contains no personally identifiable information.

## Troubleshooting

### Common Issues

1. **Directory not found**: Ensure you've extracted the dataset to the correct location
2. **Empty directories**: Some character classes may have fewer samples
3. **Corrupted images**: Occasionally, some image files may be corrupted
4. **Permission errors**: Ensure you have read permissions for all files

### Verification Script

You can use this script to check your dataset:

```bash
python -c "
import os
data_dir = 'data/by_merge'
if os.path.exists(data_dir):
    classes = [d for d in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, d))]
    print(f'Found {len(classes)} character classes')
    total_images = 0
    for cls in classes:
        cls_path = os.path.join(data_dir, cls)
        images = [f for f in os.listdir(cls_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        total_images += len(images)
        print(f'{cls}: {len(images)} images')
    print(f'Total images: {total_images}')
else:
    print('Data directory not found!')
"
```

This script will show you how many character classes and images you have in your dataset.
