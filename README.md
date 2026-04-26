# 🗜️ Image Optimizer Pro

<p align="center">
  <a href="https://github.com/himeshajayaneth/compress-tool">
    <img src="https://img.shields.io/github/stars/himeshajayaneth/compress-tool?style=social" alt="Stars">
  </a>
  <img src="https://img.shields.io/badge/version-2.0.0-blue" alt="Version">
  <img src="https://img.shields.io/badge/python-3.x-blue" alt="Python">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/platform-Windows-blue" alt="Platform">
</p>

<p align="center">
  ✨ A powerful desktop application for image compression, resizing, and format conversion ✨<br>
  Built with <b>Python + tkinter</b> 🔲 featuring a sleek dark UI inspired by Google Material Design 🎨
</p>

---

## 🌟 Features

| Feature | Description | Icon |
|---------|-------------|------|
| 🗜️ **Compress** | Reduce file size while maintaining quality | Lossy compression |
| 📏 **Resize** | Scale by dimensions or percentage with presets | Smart scaling |
| 🔄 **Convert** | Convert between JPEG, PNG, and WebP | Format conversion |
| 📚 **Batch** | Process multiple images at once | Bulk processing |
| 📱 **Responsive** | Generate multiple sizes for web/mobile | Multi-size export |
| 📥 **ZIP Export** | Download processed images as archive | Easy sharing |
| 🎨 **Dark UI** | Modern Material Design interface | Eye-friendly |
| 📊 **Progress** | Real-time progress tracking | Visual feedback |
| 🧹 **Metadata** | Strip EXIF data from images | Privacy focused |

---

## 🚀 Demo / Preview

```
┌────────────────────────────────────────────────────────────────┐
│                      💻 APPLICATION UI                       │
├────────────────────────────────────────────────────────────────┤
│  🗜️ Image Optimizer Pro     Version 2.0.0    📁 OptimizedImages│
│  ┌──────────────────────────────────────────────────────────┐ │
│  │ 🗜️ Compress │ 📏 Resize │ 🔄 Convert │ 📚 Batch │ 📱Responsive│
│  ├────────────────────┬─────────────────────────────────────┤ │
│  │                    │                                     │ │
│  │   🗜️ Compress     │         📸 Images (0 images)           │ │
│  │                    │                                     │ │
│  │   Quality          │    [📁 Browse Files] [📁 Browse]   │ │
│  │   ─────────        │    [🗑️ Clear]     [📥 Download ZIP]│ │
│  │   [███████░░] 85%  │                                     │ │
│  │                    │                                     │ │
│  │   ☐ Strip Metadata │                                     │ │
│  │   ☑ Preserve Orig │                                     │ │
│  │                    │                                     │ │
│  │  [▶️ Compress Images]                                     │ │
│  └────────────────────┴─────────────────────────────────────┘ │
│  Ready • Add images to begin                    [████████░░] 45%   │
└────────────────────────────────────────────────────────────────┘
```

---

## 📋 Requirements

| Requirement | Version | Description |
|--------------|---------|-------------|
| 🐍 Python | 3.x | Python interpreter |
| 🖼️ Pillow | Latest | Image processing library |
| 🖥️ Windows | 10/11 | Operating system |

### 📦 Install Python & Dependencies

```bash
# Check Python version
python --version

# Install Pillow
pip install pillow
```

---

## ⚡ Quick Start

### Step 1️⃣: Clone the Repository
```bash
git clone https://github.com/himeshajayaneth/compress-tool.git
cd compress-tool
```

### Step 2️⃣: Install Dependencies
```bash
pip install pillow
```

### Step 3️⃣: Run the Application
```bash
python image_optimizer.py
```

---

## 📖 How to Use (Detailed)

### 🕐 Getting Started Guide

```
┌─────────────────────────────────────────────────────────────────┐
│                 🎯 STEP-BY-STEP GUIDE               │
├─────────────────────────────────────────────────────────────────┤
│                                                         │
│  📥 STEP 1: Add Images                                  │
│     ├─ Click "Browse Files" → Select individual images│
│     └─ Click "Browse Folder" → Load all from a folder    │
│                                                         │
│  🔧 STEP 2: Select Tool                               │
│     ├─ Compress     → Reduce file size               │
│     ├─ Resize       → Change dimensions              │
│     ├─ Convert      → Change format                │
│     ├─ Batch       → Process all at once         │
│     └─ Responsive  → Generate multiple sizes    │
│                                                         │
│  ⚙️ STEP 3: Configure Settings                       │
│     ├─ Quality slider (1-100%)                     │
│     ├─ Output format (JPEG/PNG/WebP)               │
│     └─ Dimensions or scale percentage               │
│                                                         │
▶️ STEP 4: Process Images                              │
│     └─ Click the action button to start              │
│                                                         │
│  📤 STEP 5: Export                                  │
│     ├─ Download as ZIP archive                   │
│     └─ Open output folder                       │
│                                                         │
└─────────────────────────────────────────────────────────────────┘
```

### 🛠️ Tools Overview

| 🛠️ Tool | 📝 Description | ⚡ Usage |
|---------|----------------|----------|
| 🗜️ **Compress** | Reduce image file size | Quality: 1-100% |
| 📏 **Resize** | Change image dimensions | Width/Height/Scale |
| 🔄 **Convert** | Change image format | JPEG → PNG → WebP |
| 📚 **Batch** | Process multiple images | Single click |
| 📱 **Responsive** | Create multiple sizes | Thumb to Full HD |

### 📐 Resize Presets

| Preset | Dimensions | Use Case |
|--------|------------|----------|
| 🖼️ Thumbnail | 150×150 | Avatars, Icons |
| 📱 Small | 320×320 | Mobile |
| 📱 Medium | 768×768 | Tablets |
| 💻 Desktop | 1280×1024 | Standard |
| 📺 HD | 1920×1080 | Full HD |

### 📱 Responsive Sizes

| Size | Dimensions | Use Case |
|------|------------|----------|
| 🖼️ Thumbnail | 150px | Mobile thumbnails |
| 📱 Mobile | 320px | Small phones |
| 📱 Tablet | 768px | iPads, Tablets |
| 💻 Desktop | 1280px | Laptops, Monitors |
| 📺 Full HD | 1920px | 4K displays |

---

## 🎯 Supported Formats

| 📥 Input Formats | 📤 Output Formats |
|-----------------|------------------|
| JPEG (.jpg, .jpeg) | JPEG (.jpg) |
| PNG (.png) | PNG (.png) |
| WebP (.webp) | WebP (.webp) |
| BMP (.bmp) | |
| GIF (.gif) | |

---

## 💡 Use Cases

| Use Case | Recommended Tool | Settings |
|----------|-----------------|----------|
| 📸 **Photo Sharing** | Compress | Quality: 80-85% |
| 🌐 **Web Images** | Responsive | All sizes |
| 📱 **Social Media** | Convert + Resize | PNG, 1080px max |
| 📧 **Email Attachments** | Compress | Quality: 60-70% |
| 🖼️ **Print** | Resize | High quality |
| 📦 **Batch Archive** | Batch | Quality: 85% |

---

## 🔧 Technical Details

### 🏗️ Architecture

```
┌─────────────────────────────────────────┐
│           📱 APPLICATION LAYERS        │
├─────────────────────────────────────────┤
│                                         │
│  ┌─────────────────────────────────┐    │
│  │      🎨 UI Layer (tkinter)        │    │
│  │   • Headers, Toolbar, Panels    │    │
│  └─────────────────────────────────┘    │
│                    │                      │
│  ┌─────────────────────────────────┐    │
│  │    ⚙️ Business Logic Layer        │    │
│  │   • ImageOptimizerApp          │    │
│  │   • Tool switching            │    │
│  └─────────────────────────────────┘    │
│                    │                      │
│  ┌─────────────────────────────────┐    │
│  │    🖼️ Image Processing         │    │
│  │   • Pillow (PIL)               │    │
│  │   • Compress, Resize, Convert   │    │
│  └─────────────────────────────────┘    │
│                                         │
└─────────────────────────────────────────┘
```

### ⚙️ Default Settings

| Setting | Default | Description |
|---------|----------|-------------|
| 🖼️ Quality | 85% | Compression quality |
| 📏 Window Size | 1200×800 | UI size |
| 📁 Min Size | 1000×700 | Minimum window |
| 📂 Output | OptimizedImages/ | Output folder |
| 🎨 Theme | Dark | UI theme |

### 🔑 Key Functions

| Function | Description | Parameters |
|----------|-------------|------------|
| `compress_images()` | Compress with quality | quality (1-100), strip_meta |
| `resize_images()` | Resize by dimensions | width, height, scale |
| `convert_images()` | Convert format | format, quality |
| `batch_process()` | Batch operation | quality |
| `generate_responsive()` | Multi-size | sizes list |

### 🎨 Color Palette

| Color | Hex | Usage |
|-------|-----|-------|
| 🔵 Primary BG | `#1a1a2e` | Main background |
| 🔷 Secondary BG | `#16213e` | Cards, panels |
| 💜 Accent | `#6366f1` | Buttons, active |
| 🟢 Success | `#10b981` | Success actions |
| ⚠️ Warning | `#f59e0b` | Warnings |
| ❌ Danger | `#ef4444` | Delete, clear |

---

## 📂 Output

### 📁 Output Directory
```
~/Desktop/OptimizedImages/
```

### 📝 File Naming Convention

| Operation | Output Filename | Example |
|------------|----------------|---------|
| Compress | `{name}_optimized.jpg` | photo_optimized.jpg |
| Resize | `{name}_resized.jpg` | photo_resized.jpg |
| Convert | `{name}_converted.{fmt}` | photo_converted.png |
| Batch | `{name}_batch.jpg` | photo_batch.jpg |
| Responsive | `{name}_{size}.jpg` | photo_thumbnail.jpg |

---

## ❓ FAQ (Frequently Asked Questions)

### General Questions

| Question | Answer |
|----------|--------|
| ❓ **Is it free?** | Yes! MIT Licensed |
| ❓ **Is it safe?** | Yes! No data leaves your device |
| ❓ **Does it work offline?** | Yes! 100% offline |
| ❓ **What OS is supported?** | Windows 10/11 |
| ❓ **Can I preserve originals?** | Yes! Check "Preserve Original" |

### Technical Questions

| Question | Answer |
|----------|--------|
| ❓ **Best quality for web?** | 80-85% |
| ❓ **Best for email?** | 60-70% |
| ❓ **Does it remove EXIF?** | Yes! Check "Strip Metadata" |
| ❓ **Format for transparency?** | Use PNG |
| ❓ **Format for web?** | Use WebP |

---

## 🔧 Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| 🚫 Python not found | Install Python 3.x |
| 🚫 Pillow not installed | `pip install pillow` |
| 🚫 No images loaded | Browse files first |
| 🚫 Error opening file | Check file permissions |
| 🚫 Slow processing | Reduce batch size |

### Installation Errors

```bash
# Error: pip not found
python -m pip install pillow

# Error: Permission denied
pip install pillow --user

# Update pip first
python -m pip install --upgrade pip
```

---

## 📊 Performance Tips

| Tip | Benefit |
|-----|----------|
| 💾 Close other apps | Faster processing |
| 📁 Use SSD | Quick save times |
| 🎯 Right quality | Balance size/quality |
| 📦 Batch process | Save time |

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. 🍴 Fork the repository
2. 🔧 Create your feature branch
3. 📝 Commit your changes
4. 📤 Push to the branch
5. 🔃 Create Pull Request

---

## 📜 License

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
</p>

```
MIT License
Copyright (c) 2024 Himesha Jayaneth
```

---

## 👩‍💻 Author

<p align="center">
  <strong>Himesha Jayaneth</strong> 👋<br><br>
  <a href="https://github.com/himeshajayaneth">
    <img src="https://img.shields.io/badge/GitHub-Follow-blue?logo=github" alt="GitHub">
  </a>
  <a href="https://github.com/himeshajayaneth/compress-tool">
    <img src="https://img.shields.io/badge/Repo-Star-blue?logo=github" alt="Stars">
  </a>
</p>

---

## 🙏 Acknowledgments

| Library | Purpose | Link |
|----------|---------|------|
| 🖼️ Pillow | Image processing | [python-pillow.org](https://python-pillow.org/) |
| 🐍 Python | Programming language | [python.org](https://python.org/) |
| 🎨 tkinter | GUI framework | Python stdlib |

---

## 📝 Changelog

### v2.0.0 (Current)
- ✅ Added responsive image generation
- ✅ Added ZIP export
- ✅ Improved dark UI
- ✅ Added progress bar
- ✅ Added metadata stripping

### v1.0.0
- ✅ Initial release
- ✅ Basic compression
- ✅ Resize tool
- ✅ Convert tool

---

## 📬 Contact

- 🌐 GitHub: [himeshajayaneth](https://github.com/himeshajayaneth)
- 📧 Email: Check GitHub profile

---

<p align="center">
  <strong>⭐ Don't forget to star this repository if you found it helpful! ⭐</strong><br><br>
  Made with ❤️ by <a href="https://github.com/himeshajayaneth">Himesha Jayaneth</a>
</p>