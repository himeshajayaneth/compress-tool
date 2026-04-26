# 🗜️ Image Optimizer Pro

<p align="center">
  <img src="https://img.shields.io/badge/version-2.0.0-blue" alt="Version">
  <img src="https://img.shields.io/badge/python-3.x-blue" alt="Python">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
</p>

<p align="center">
  ✨ A modern desktop application for image compression, resizing, and format conversion ✨<br>
  Built with Python + tkinter 🔲 featuring a sleek dark UI inspired by Google Material Design
</p>

---

## 🌟 Features

| Feature | Description |
|---------|-------------|
| 🗜️ **Compress** | Reduce file size while maintaining quality |
| 📏 **Resize** | Scale by dimensions or percentage with presets |
| 🔄 **Convert** | Convert between JPEG, PNG, and WebP |
| 📚 **Batch** | Process multiple images at once |
| 📱 **Responsive** | Generate multiple sizes for web/mobile |
| 📥 **ZIP Export** | Download processed images as archive |
| 🎨 **Dark UI** | Modern Material Design interface |

---

## 📋 Requirements

```
🐍 Python 3.x
🖼️  Pillow (PIL)
```

---

## ⚡ Quick Start

### 1️⃣ Clone the repository
```bash
git clone https://github.com/himeshajayaneth/compress-tool.git
cd compress-tool
```

### 2️⃣ Install dependencies
```bash
pip install pillow
```

### 3️⃣ Run the app
```bash
python image_optimizer.py
```

---

## 📖 How to Use

```
┌─────────────────────────────────────────────────────────┐
│                    🚀 GETTING STARTED                  │
├─────────────────────────────────────────────────────────┤
│  1️⃣  Add Images     → Browse Files or Folder          │
│  2️⃣  Select Tool   → Compress/Resize/Convert/etc   │
│  3️⃣  Configure     → Quality, Size, Format           │
│  4️⃣  Process       → Click action button             │
│  5️⃣  Export        → ZIP download or open folder   │
└─────────────────────────────────────────────────────────┘
```

### 🛠️ Tools Overview

| 🛠️ Tool | 📝 Description |
|---------|----------------|
| 🗜️ **Compress** | Reduce image size with quality slider (1-100%) |
| 📏 **Resize** | Set custom dimensions or scale % |
| 🔄 **Convert** | Change format: JPEG → PNG → WebP |
| 📚 **Batch** | Process all images at once |
| 📱 **Responsive** | Generate all sizes (Thumb → Full HD) |

---

## 🎯 Supported Formats

| 📥 Input | 📤 Output |
|----------|----------|
| JPEG, PNG, WebP, BMP, GIF | JPEG, PNG, WebP |

---

## 🔧 Technical Details

### 🏗️ Architecture
- **GUI**: tkinter (Python stdlib)
- **Image Processing**: Pillow (PIL Fork)
- **Default Quality**: 85%
- **Output Folder**: `~/Desktop/OptimizedImages`

### ⚙️ Default Settings
| Setting | Value |
|---------|-------|
| Window Size | 1200×800 (min: 1000×700) |
| Quality | 85% |
| Output | `Desktop/OptimizedImages/` |

### 🔑 Key Functions
```python
compress_images()      # Compress with quality control
resize_images()        # Resize by dimensions or scale
convert_images()      # Convert between formats
batch_process()       # Process multiple images
generate_responsive() # Create multiple sizes
```

---

## 📂 Output

Processed images saved to:
```
📁 ~/Desktop/OptimizedImages/
```

| Suffix | Type |
|--------|------|
| `_optimized.jpg` | Compressed |
| `_resized.jpg` | Resized |
| `_converted.{fmt}` | Converted |
| `_batch.jpg` | Batch processed |

---

## 💻 Platform

<p align="center">
  <img src="https://img.shields.io/badge/platform-Windows-blue" alt="Windows">
</p>

---

## 📜 License

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
</p>

MIT License

---

## 👩‍💻 Author

<p align="center">
  <strong>Himesha Jayaneth</strong><br>
  <a href="https://github.com/himeshajayaneth">
    <img src="https://img.shields.io/badge/GitHub-Follow-blue?logo=github" alt="GitHub">
  </a>
</p>

---

## 🙏 Acknowledgments

- [Pillow](https://python-pillow.org/) 🖼️ - Python Imaging Library

---

<p align="center">
  ⭐ Star this repo if you found it helpful! ⭐
</p>