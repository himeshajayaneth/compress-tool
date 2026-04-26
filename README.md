# Image Optimizer Pro

A modern desktop application for image compression, resizing, and format conversion. Built with Python and tkinter, featuring a sleek dark UI inspired by Google Material Design.

![Version](https://img.shields.io/badge/version-2.0.0-blue)
![Python](https://img.shields.io/badge/python-3.x-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Features

- **Compress Images** - Reduce file size while maintaining quality
- **Resize Images** - Scale by dimensions or percentage with presets
- **Convert Formats** - Convert between JPEG, PNG, and WebP
- **Batch Processing** - Process multiple images at once
- **Responsive Images** - Generate multiple sizes for web/mobile
- **ZIP Download** - Export processed images as ZIP archive
- **Modern UI** - Dark theme with Material Design inspired interface

## Requirements

- Python 3.x
- Pillow (PIL)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/himeshajayaneth/compress-tool.git
cd compress-tool
```

2. Install dependencies:
```bash
pip install pillow
```

## Usage

Run the application:
```bash
python image_optimizer.py
```

### Getting Started

1. **Add Images**: Click "Browse Files" to select individual images or "Browse Folder" to load all images from a folder
2. **Select Tool**: Choose a tool from the toolbar (Compress, Resize, Convert, Batch, Responsive)
3. **Configure**: Adjust settings like quality, dimensions, or target format
4. **Process**: Click the action button to process your images
5. **Export**: Download processed images as ZIP or open the output folder

### Tools Overview

| Tool | Description |
|------|-------------|
| Compress | Reduce image file size with quality slider (1-100%) |
| Resize | Set custom dimensions or scale by percentage |
| Convert | Change image format to JPEG, PNG, or WebP |
| Batch | Process all loaded images with one operation |
| Responsive | Generate multiple sizes (Thumbnail to Full HD) |

### Supported Formats

- Input: JPEG, PNG, WebP, BMP, GIF
- Output: JPEG, PNG, WebP

## Technical Details

### Architecture

- **GUI Framework**: tkinter (Python standard library)
- **Image Processing**: Pillow (PIL Fork)
- **Default Quality**: 85%
- **Output Directory**: `~/Desktop/OptimizedImages`

### Key Classes

| Class | Purpose |
|-------|---------|
| `ImageOptimizerApp` | Main application class managing UI and operations |
| `COLORS` | Color palette dictionary for theming |

### Default Settings

- Window Size: 1200x800 (min: 1000x700)
- Default Output: `C:\Users\[User]\Desktop\OptimizedImages`
- Default Quality: 85%

### Core Functions

- `compress_images()` - Compress with quality control
- `resize_images()` - Resize by dimensions or scale
- `convert_images()` - Convert between formats
- `batch_process()` - Process multiple images
- `generate_responsive()` - Create multiple sizes

## Output

Processed images are saved to:
```
~/Desktop/OptimizedImages/
```

Files are named with suffixes:
- `_optimized.jpg` - Compressed images
- `_resized.jpg` - Resized images
- `_converted.{fmt}` - Converted images
- `_batch.jpg` - Batch processed

## License

MIT License

## Author

[Himesha Jayaneth](https://github.com/himeshajayaneth)

## Acknowledgments

- [Pillow](https://python-pillow.org/) - Python Imaging Library