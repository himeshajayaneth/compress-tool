"""
Image Optimizer Pro - Desktop Application
Modern image compression and optimization tool with Google Material Design inspired UI
"""

import os
import sys
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image
import zipfile

APP_NAME = "Image Optimizer Pro"
VERSION = "2.0.0"

DEFAULT_QUALITY = 85
OUTPUT_DIR = os.path.join(os.path.expanduser("~"), "Desktop", "OptimizedImages")

COLORS = {
    "bg_primary": "#1a1a2e",
    "bg_secondary": "#16213e",
    "bg_card": "#252542",
    "bg_hover": "#303050",
    "accent": "#6366f1",
    "accent_hover": "#4f46e5",
    "success": "#10b981",
    "warning": "#f59e0b",
    "danger": "#ef4444",
    "text_primary": "#ffffff",
    "text_secondary": "#a1a1aa",
    "border": "#3f3f5a"
}

class ImageOptimizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title(f"{APP_NAME} {VERSION}")
        self.root.geometry("1200x800")
        self.root.minsize(1000, 700)
        self.root.configure(bg=COLORS["bg_primary"])
        
        self.images = []
        self.processed_images = []
        self.output_dir = OUTPUT_DIR
        os.makedirs(self.output_dir, exist_ok=True)
        
        self.current_tool = "compress"
        self.left_panel_widgets = {}
        self.create_ui()
    
    def create_ui(self):
        main_container = tk.Frame(self.root, bg=COLORS["bg_primary"])
        main_container.pack(fill=tk.BOTH, expand=True)
        
        header = self.create_header(main_container)
        header.pack(fill=tk.X, padx=20, pady=(15, 10))
        
        toolbar = self.create_toolbar(main_container)
        toolbar.pack(fill=tk.X, padx=20, pady=(0, 15))
        
        status = self.create_status(main_container)
        status.pack(fill=tk.X, padx=20, pady=(0, 15))
        
        content = self.create_content(main_container)
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))
    
    def create_header(self, parent):
        header = tk.Frame(parent, bg=COLORS["bg_primary"])
        
        logo_frame = tk.Frame(header, bg=COLORS["bg_primary"])
        logo_frame.pack(side=tk.LEFT)
        
        tk.Label(logo_frame, text="🗜️", font=("Segoe UI", 28), 
               bg=COLORS["bg_primary"]).pack(side=tk.LEFT, padx=(0, 10))
        
        title_frame = tk.Frame(logo_frame, bg=COLORS["bg_primary"])
        title_frame.pack(side=tk.LEFT)
        
        tk.Label(title_frame, text=APP_NAME, font=("Segoe UI", 18, "bold"),
               bg=COLORS["bg_primary"], fg=COLORS["text_primary"]).pack(anchor=tk.W)
        tk.Label(title_frame, text=f"Version {VERSION}", font=("Segoe UI", 9),
               bg=COLORS["bg_primary"], fg=COLORS["text_secondary"]).pack(anchor=tk.W)
        
        right_frame = tk.Frame(header, bg=COLORS["bg_primary"])
        right_frame.pack(side=tk.RIGHT)
        
        tk.Button(right_frame, text=f"📁 {os.path.basename(self.output_dir)}", 
                            command=self.open_output_folder,
                            bg=COLORS["bg_card"], fg=COLORS["text_secondary"],
                            font=("Segoe UI", 9), bd=0, padx=12, pady=6,
                            cursor="hand2", relief=tk.FLAT).pack()
        
        return header
    
    def create_toolbar(self, parent):
        toolbar = tk.Frame(parent, bg=COLORS["bg_card"], bd=0)
        toolbar.pack_propagate(False)
        toolbar.configure(height=50)
        
        self.tool_buttons = {}
        tools = [
            ("compress", "🗜️ Compress"),
            ("resize", "📏 Resize"),
            ("convert", "🔄 Convert"),
            ("batch", "📚 Batch"),
            ("responsive", "📱 Responsive")
        ]
        
        for tool_id, tool_text in tools:
            btn = tk.Button(toolbar, text=tool_text,
                        command=lambda t=tool_id: self.switch_tool(t),
                        bg=COLORS["accent"] if tool_id == self.current_tool else COLORS["bg_card"],
                        fg=COLORS["text_primary"],
                        font=("Segoe UI", 10),
                        bd=0, padx=20, pady=12,
                        cursor="hand2", relief=tk.FLAT)
            btn.pack(side=tk.LEFT, padx=2)
            self.tool_buttons[tool_id] = btn
            btn.bind("<Enter>", lambda e, b=btn: b.configure(bg=COLORS["bg_hover"]))
            btn.bind("<Leave>", lambda e, b=btn, t=tool_id: b.configure(
                bg=COLORS["accent"] if t == self.current_tool else COLORS["bg_card"]))
        
        return toolbar
    
    def switch_tool(self, tool_id):
        self.current_tool = tool_id
        for tid, btn in self.tool_buttons.items():
            btn.configure(bg=COLORS["accent"] if tid == tool_id else COLORS["bg_card"])
        
        for widget in self.left_panel_widgets.values():
            widget.pack_forget()
        
        if tool_id in self.left_panel_widgets:
            self.left_panel_widgets[tool_id].pack(fill=tk.BOTH, expand=True, padx=(0, 15))
        
        status_text = {
            "compress": "Compress mode • Adjust quality and compress images",
            "resize": "Resize mode • Resize images by dimensions or scale",
            "convert": "Convert mode • Change image format",
            "batch": "Batch mode • Process multiple images at once",
            "responsive": "Responsive mode • Generate multiple sizes for web"
        }
        self.status_bar.config(text=status_text.get(tool_id, ""))
    
    def create_content(self, parent):
        content = tk.Frame(parent, bg=COLORS["bg_primary"])
        
        self.left_panel_container = tk.Frame(content, bg=COLORS["bg_primary"])
        self.left_panel_container.pack(side=tk.LEFT, fill=tk.BOTH)
        
        self.create_compress_panel()
        self.create_resize_panel()
        self.create_convert_panel()
        self.create_batch_panel()
        self.create_responsive_panel()
        
        self.switch_tool("compress")
        
        right_panel = self.create_right_panel(content)
        right_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        return content
    
    def create_compress_panel(self):
        panel = tk.Frame(self.left_panel_container, bg=COLORS["bg_card"], width=320)
        panel.pack_propagate(False)
        self.left_panel_widgets["compress"] = panel
        
        title = tk.Label(panel, text="🗜️ Compress", font=("Segoe UI", 14, "bold"),
                        bg=COLORS["bg_card"], fg=COLORS["text_primary"])
        title.pack(pady=(10, 15))
        
        tk.Label(panel, text="Quality", bg=COLORS["bg_card"], 
               fg=COLORS["text_secondary"], font=("Segoe UI", 9)).pack(anchor=tk.W)
        
        self.qualityslider = tk.Scale(panel, from_=1, to=100, 
                                   orient=tk.HORIZONTAL,
                                   bg=COLORS["bg_card"], fg=COLORS["text_primary"],
                                   highlightthickness=0, troughcolor=COLORS["bg_hover"],
                                   length=250, showvalue=0)
        self.qualityslider.set(DEFAULT_QUALITY)
        self.qualityslider.pack(fill=tk.X, pady=5)
        
        self.quality_label = tk.Label(panel, text=f"Quality: {DEFAULT_QUALITY}%",
                                bg=COLORS["bg_card"], fg=COLORS["accent"],
                                font=("Segoe UI", 10, "bold"))
        self.quality_label.pack()
        self.qualityslider.bind("<Motion>", lambda e: self.quality_label.configure(
            text=f"Quality: {self.qualityslider.get()}%"))
        
        self.strip_meta_var = tk.BooleanVar()
        tk.Checkbutton(panel, text="🧹 Strip Metadata (EXIF)",
                    variable=self.strip_meta_var, bg=COLORS["bg_card"],
                    fg=COLORS["text_primary"], selectcolor=COLORS["accent"],
                    activebackground=COLORS["bg_card"]).pack(anchor=tk.W, pady=10)
        
        self.preserve_var = tk.BooleanVar(value=True)
        tk.Checkbutton(panel, text="💾 Preserve Original",
                    variable=self.preserve_var, bg=COLORS["bg_card"],
                    fg=COLORS["text_primary"], selectcolor=COLORS["accent"],
                    activebackground=COLORS["bg_card"]).pack(anchor=tk.W)
        
        tk.Label(panel, text="", bg=COLORS["bg_card"]).pack(pady=5)
        
        tk.Button(panel, text="▶️ Compress Images", command=self.compress_images,
                bg=COLORS["success"], fg=COLORS["text_primary"],
                font=("Segoe UI", 11, "bold"),
                bd=0, padx=20, pady=10,
                cursor="hand2", relief=tk.FLAT).pack(fill=tk.X, pady=5)
    
    def create_resize_panel(self):
        panel = tk.Frame(self.left_panel_container, bg=COLORS["bg_card"], width=320)
        panel.pack_propagate(False)
        self.left_panel_widgets["resize"] = panel
        
        title = tk.Label(panel, text="📏 Resize", font=("Segoe UI", 14, "bold"),
                        bg=COLORS["bg_card"], fg=COLORS["text_primary"])
        title.pack(pady=(10, 15))
        
        tk.Label(panel, text="Width (px)", bg=COLORS["bg_card"], 
               fg=COLORS["text_secondary"], font=("Segoe UI", 9)).pack(anchor=tk.W)
        
        self.resize_width = tk.Entry(panel, bg=COLORS["bg_primary"], fg=COLORS["text_primary"],
                                   font=("Segoe UI", 10), bd=0, relief=tk.FLAT)
        self.resize_width.pack(fill=tk.X, pady=5)
        self.resize_width.insert(0, "800")
        
        tk.Label(panel, text="Height (px)", bg=COLORS["bg_card"], 
               fg=COLORS["text_secondary"], font=("Segoe UI", 9)).pack(anchor=tk.W, pady=(10, 0))
        
        self.resize_height = tk.Entry(panel, bg=COLORS["bg_primary"], fg=COLORS["text_primary"],
                                      font=("Segoe UI", 10), bd=0, relief=tk.FLAT)
        self.resize_height.pack(fill=tk.X, pady=5)
        self.resize_height.insert(0, "600")
        
        tk.Label(panel, text="Or Scale (%)", bg=COLORS["bg_card"], 
               fg=COLORS["text_secondary"], font=("Segoe UI", 9)).pack(anchor=tk.W, pady=(10, 0))
        
        self.resize_scale = tk.Entry(panel, bg=COLORS["bg_primary"], fg=COLORS["text_primary"],
                                    font=("Segoe UI", 10), bd=0, relief=tk.FLAT)
        self.resize_scale.pack(fill=tk.X, pady=5)
        
        presets = tk.Frame(panel, bg=COLORS["bg_card"])
        presets.pack(fill=tk.X, pady=10)
        
        for name, w, h in [("Thumb", 150, 150), ("Small", 320, 320), ("Medium", 768, 768)]:
            tk.Button(presets, text=name, command=lambda n=name, w=w, h=h: self.set_resize_preset(w, h),
                   bg=COLORS["bg_hover"], fg=COLORS["text_primary"],
                   font=("Segoe UI", 8), bd=0, padx=8, pady=4,
                   cursor="hand2").pack(side=tk.LEFT, padx=2)
        
        for name, w, h in [("Large", 1280, 1024), ("HD", 1920, 1080)]:
            tk.Button(presets, text=name, command=lambda n=name, w=w, h=h: self.set_resize_preset(w, h),
                   bg=COLORS["bg_hover"], fg=COLORS["text_primary"],
                   font=("Segoe UI", 8), bd=0, padx=8, pady=4,
                   cursor="hand2").pack(side=tk.LEFT, padx=2)
        
        tk.Button(panel, text="▶️ Resize Images", command=self.resize_images,
                bg=COLORS["success"], fg=COLORS["text_primary"],
                font=("Segoe UI", 11, "bold"),
                bd=0, padx=20, pady=10,
                cursor="hand2", relief=tk.FLAT).pack(fill=tk.X, pady=5)
    
    def create_convert_panel(self):
        panel = tk.Frame(self.left_panel_container, bg=COLORS["bg_card"], width=320)
        panel.pack_propagate(False)
        self.left_panel_widgets["convert"] = panel
        
        title = tk.Label(panel, text="🔄 Convert", font=("Segoe UI", 14, "bold"),
                        bg=COLORS["bg_card"], fg=COLORS["text_primary"])
        title.pack(pady=(10, 15))
        
        tk.Label(panel, text="Target Format", bg=COLORS["bg_card"], 
               fg=COLORS["text_secondary"], font=("Segoe UI", 9)).pack(anchor=tk.W)
        
        self.convert_format = tk.StringVar(value="JPEG")
        fmt_frame = tk.Frame(panel, bg=COLORS["bg_card"])
        fmt_frame.pack(fill=tk.X, pady=5)
        
        for fmt in ["JPEG", "PNG", "WebP"]:
            tk.Radiobutton(fmt_frame, text=fmt, bg=COLORS["bg_card"],
                        fg=COLORS["text_primary"], variable=self.convert_format,
                        value=fmt, selectcolor=COLORS["accent"]).pack(side=tk.LEFT, padx=10)
        
        tk.Label(panel, text="Quality", bg=COLORS["bg_card"], 
               fg=COLORS["text_secondary"], font=("Segoe UI", 9)).pack(anchor=tk.W, pady=(15, 0))
        
        self.convert_quality = tk.Scale(panel, from_=1, to=100, 
                                        orient=tk.HORIZONTAL,
                                        bg=COLORS["bg_card"], fg=COLORS["text_primary"],
                                        highlightthickness=0, troughcolor=COLORS["bg_hover"],
                                        length=250, showvalue=0)
        self.convert_quality.set(DEFAULT_QUALITY)
        self.convert_quality.pack(fill=tk.X, pady=5)
        
        tk.Label(panel, text=self.convert_quality.get(), bg=COLORS["bg_card"], 
               fg=COLORS["accent"], font=("Segoe UI", 10, "bold")).pack()
        
        self.preserve_convert = tk.BooleanVar(value=True)
        tk.Checkbutton(panel, text="💾 Preserve Original",
                    variable=self.preserve_convert, bg=COLORS["bg_card"],
                    fg=COLORS["text_primary"], selectcolor=COLORS["accent"],
                    activebackground=COLORS["bg_card"]).pack(anchor=tk.W, pady=10)
        
        tk.Button(panel, text="▶️ Convert Images", command=self.convert_images,
                bg=COLORS["success"], fg=COLORS["text_primary"],
                font=("Segoe UI", 11, "bold"),
                bd=0, padx=20, pady=10,
                cursor="hand2", relief=tk.FLAT).pack(fill=tk.X, pady=5)
    
    def create_batch_panel(self):
        panel = tk.Frame(self.left_panel_container, bg=COLORS["bg_card"], width=320)
        panel.pack_propagate(False)
        self.left_panel_widgets["batch"] = panel
        
        title = tk.Label(panel, text="📚 Batch Process", font=("Segoe UI", 14, "bold"),
                        bg=COLORS["bg_card"], fg=COLORS["text_primary"])
        title.pack(pady=(10, 15))
        
        tk.Label(panel, text="Operation", bg=COLORS["bg_card"], 
               fg=COLORS["text_secondary"], font=("Segoe UI", 9)).pack(anchor=tk.W)
        
        self.batch_operation = tk.StringVar(value="compress")
        op_frame = tk.Frame(panel, bg=COLORS["bg_card"])
        op_frame.pack(fill=tk.X, pady=5)
        
        for op in [("compress", "Compress"), ("resize", "Resize"), ("convert", "Convert")]:
            tk.Radiobutton(op_frame, text=op[1], bg=COLORS["bg_card"],
                         fg=COLORS["text_primary"], variable=self.batch_operation,
                         value=op[0], selectcolor=COLORS["accent"]).pack(side=tk.LEFT, padx=10)
        
        tk.Label(panel, text="Quality", bg=COLORS["bg_card"], 
               fg=COLORS["text_secondary"], font=("Segoe UI", 9)).pack(anchor=tk.W, pady=(10, 0))
        
        self.batch_quality = tk.Scale(panel, from_=1, to=100, 
                                     orient=tk.HORIZONTAL,
                                     bg=COLORS["bg_card"], fg=COLORS["text_primary"],
                                     highlightthickness=0, troughcolor=COLORS["bg_hover"],
                                     length=250, showvalue=0)
        self.batch_quality.set(DEFAULT_QUALITY)
        self.batch_quality.pack(fill=tk.X, pady=5)
        
        tk.Button(panel, text="▶️ Process All Images", command=self.batch_process,
                bg=COLORS["success"], fg=COLORS["text_primary"],
                font=("Segoe UI", 11, "bold"),
                bd=0, padx=20, pady=10,
                cursor="hand2", relief=tk.FLAT).pack(fill=tk.X, pady=5)
    
    def create_responsive_panel(self):
        panel = tk.Frame(self.left_panel_container, bg=COLORS["bg_card"], width=320)
        panel.pack_propagate(False)
        self.left_panel_widgets["responsive"] = panel
        
        title = tk.Label(panel, text="📱 Responsive", font=("Segoe UI", 14, "bold"),
                        bg=COLORS["bg_card"], fg=COLORS["text_primary"])
        title.pack(pady=(10, 15))
        
        tk.Label(panel, text="Select sizes to generate:", bg=COLORS["bg_card"], 
               fg=COLORS["text_secondary"], font=("Segoe UI", 9)).pack(anchor=tk.W, pady=5)
        
        self.responsive_vars = {}
        sizes = [("Thumbnail", 150), ("Mobile", 320), ("Tablet", 768), 
                ("Desktop", 1280), ("Full HD", 1920)]
        
        for name, size in sizes:
            var = tk.BooleanVar(value=True)
            self.responsive_vars[name] = var
            tk.Checkbutton(panel, text=f"{name} ({size}px)", bg=COLORS["bg_card"],
                        fg=COLORS["text_primary"], variable=var,
                        selectcolor=COLORS["accent"],
                        activebackground=COLORS["bg_card"]).pack(anchor=tk.W)
        
        tk.Label(panel, text="", bg=COLORS["bg_card"]).pack(pady=5)
        
        tk.Button(panel, text="▶️ Generate All Sizes", command=self.generate_responsive,
                bg=COLORS["success"], fg=COLORS["text_primary"],
                font=("Segoe UI", 11, "bold"),
                bd=0, padx=20, pady=10,
                cursor="hand2", relief=tk.FLAT).pack(fill=tk.X, pady=5)
    
    def create_right_panel(self, parent):
        panel = tk.Frame(parent, bg=COLORS["bg_primary"])
        
        title_row = tk.Frame(panel, bg=COLORS["bg_primary"])
        title_row.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(title_row, text="📸 Images",
                              font=("Segoe UI", 14, "bold"),
                              bg=COLORS["bg_primary"], fg=COLORS["text_primary"]).pack(side=tk.LEFT)
        
        self.image_count = tk.Label(title_row, text="(0 images)",
                         font=("Segoe UI", 10),
                         bg=COLORS["bg_primary"], fg=COLORS["text_secondary"])
        self.image_count.pack(side=tk.LEFT, padx=5)
        
        list_frame = tk.Frame(panel, bg=COLORS["bg_hover"], bd=0)
        list_frame.pack(fill=tk.BOTH, expand=True)
        
        self.image_listbox = tk.Listbox(list_frame, bg=COLORS["bg_card"],
                                   fg=COLORS["text_primary"],
                                   font=("Segoe UI", 10),
                                   selectbackground=COLORS["accent"],
                                   bd=0, highlightthickness=0)
        self.image_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        scrollbar = tk.Scrollbar(list_frame, bg=COLORS["bg_card"], troughcolor=COLORS["bg_card"])
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.image_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.image_listbox.yview)
        
        btn_row = tk.Frame(panel, bg=COLORS["bg_primary"])
        btn_row.pack(fill=tk.X, pady=(10, 0))
        
        tk.Button(btn_row, text="📁 Browse Files",
                command=self.select_files,
                bg=COLORS["accent"], fg=COLORS["text_primary"],
                font=("Segoe UI", 10),
                bd=0, padx=15, pady=10,
                cursor="hand2", relief=tk.FLAT).pack(side=tk.LEFT, padx=2)
        
        tk.Button(btn_row, text="📁 Browse Folder",
                command=self.select_folder,
                bg=COLORS["bg_card"], fg=COLORS["text_primary"],
                font=("Segoe UI", 10),
                bd=0, padx=15, pady=10,
                cursor="hand2", relief=tk.FLAT).pack(side=tk.LEFT, padx=2)
        
        tk.Button(btn_row, text="🗑️ Clear",
                command=self.clear_images,
                bg=COLORS["danger"], fg=COLORS["text_primary"],
                font=("Segoe UI", 10),
                bd=0, padx=15, pady=10,
                cursor="hand2", relief=tk.FLAT).pack(side=tk.LEFT, padx=2)
        
        tk.Button(btn_row, text="📥 Download ZIP",
                command=self.download_zip,
                bg=COLORS["bg_card"], fg=COLORS["text_primary"],
                font=("Segoe UI", 10),
                bd=0, padx=15, pady=10,
                cursor="hand2", relief=tk.FLAT).pack(side=tk.RIGHT, padx=2)
        
        return panel
    
    def create_status(self, parent):
        status = tk.Frame(parent, bg=COLORS["bg_card"], height=35)
        status.pack_propagate(False)
        
        self.status_bar = tk.Label(status, text="Ready • Add images to begin",
                            bg=COLORS["bg_card"], fg=COLORS["text_secondary"],
                            font=("Segoe UI", 9), anchor=tk.W)
        self.status_bar.pack(side=tk.LEFT, padx=10)
        
        self.progress_bar = ttk.Progressbar(status, mode="determinate",
                                  length=200, style="Custom.Horizontal.TProgressbar")
        self.progress_bar.pack(side=tk.RIGHT, padx=10)
        
        return status
    
    def select_files(self):
        files = filedialog.askopenfilenames(title="Select Images",
                                        filetypes=[("Images", "*.jpg *.jpeg *.png *.webp *.bmp *.gif")])
        if files:
            self.add_images(files)
    
    def select_folder(self):
        folder = filedialog.askdirectory(title="Select Folder with Images")
        if folder:
            exts = ('.jpg', '.jpeg', '.png', '.webp', '.bmp', '.gif')
            files = [os.path.join(folder, f) for f in os.listdir(folder) 
                    if f.lower().endswith(exts)]
            if files:
                self.add_images(files)
                self.status_bar.config(text=f"Loaded {len(files)} images from folder")
            else:
                messagebox.showinfo("No Images", "No images found in folder")
    
    def add_images(self, files):
        for f in files:
            if f not in self.images:
                self.images.append(f)
        self.update_list()
        self.image_count.config(text=f"({len(self.images)} images)")
        self.status_bar.config(text=f"Loaded {len(self.images)} image(s)")
    
    def clear_images(self):
        self.images = []
        self.update_list()
        self.image_count.config(text="(0 images)")
        self.status_bar.config(text="Cleared all images")
    
    def update_list(self):
        self.image_listbox.delete(0, tk.END)
        for img in self.images:
            self.image_listbox.insert(tk.END, os.path.basename(img))
    
    def set_resize_preset(self, w, h):
        self.resize_width.delete(0, tk.END)
        self.resize_width.insert(0, str(w))
        self.resize_height.delete(0, tk.END)
        self.resize_height.insert(0, str(h))
    
    def process_images(self):
        if self.current_tool == "compress":
            self.compress_images()
        elif self.current_tool == "resize":
            self.resize_images()
        elif self.current_tool == "convert":
            self.convert_images()
        elif self.current_tool == "batch":
            self.batch_process()
        elif self.current_tool == "responsive":
            self.generate_responsive()
    
    def compress_images(self):
        if not self.images:
            messagebox.showwarning("No Images", "Please add images first")
            return
        
        quality = self.qualityslider.get()
        strip = self.strip_meta_var.get()
        preserve = self.preserve_var.get()
        
        self.status_bar.config(text="Compressing...")
        
        os.makedirs(self.output_dir, exist_ok=True)
        saved = 0
        
        for i, img_path in enumerate(self.images):
            try:
                img = Image.open(img_path)
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
                
                name = os.path.splitext(os.path.basename(img_path))[0]
                out_name = f"{name}_optimized.jpg" if preserve else f"{name}.jpg"
                out_path = os.path.join(self.output_dir, out_name)
                
                img.save(out_path, "JPEG", quality=quality, optimize=True)
                
                saved += 1
                progress = ((i + 1) / len(self.images)) * 100
                self.progress_bar.configure(value=progress)
                self.root.update_idletasks()
            except Exception as e:
                print(f"Error: {e}")
        
        self.progress_bar.configure(value=0)
        self.status_bar.config(text=f"Compressed {saved} images")
        messagebox.showinfo("Complete", f"Compressed {saved} images!\nSaved to: {self.output_dir}")
    
    def resize_images(self):
        if not self.images:
            messagebox.showwarning("No Images", "Please add images first")
            return
        
        width = self.resize_width.get()
        height = self.resize_height.get()
        scale = self.resize_scale.get()
        
        self.status_bar.config(text="Resizing...")
        
        os.makedirs(self.output_dir, exist_ok=True)
        saved = 0
        
        for i, img_path in enumerate(self.images):
            try:
                img = Image.open(img_path)
                
                if scale:
                    w = int(img.width * int(scale) / 100)
                    h = int(img.height * int(scale) / 100)
                else:
                    w = int(width) if width else None
                    h = int(height) if height else None
                
                img = img.resize((w, h), Image.Resampling.LANCZOS)
                
                name = os.path.splitext(os.path.basename(img_path))[0]
                out_path = os.path.join(self.output_dir, f"{name}_resized.jpg")
                
                img.save(out_path, "JPEG", quality=DEFAULT_QUALITY)
                saved += 1
                
                progress = ((i + 1) / len(self.images)) * 100
                self.progress_bar.configure(value=progress)
                self.root.update_idletasks()
            except Exception as e:
                print(f"Error: {e}")
        
        self.progress_bar.configure(value=0)
        self.status_bar.config(text=f"Resized {saved} images")
        messagebox.showinfo("Complete", f"Resized {saved} images!\nSaved to: {self.output_dir}")
    
    def convert_images(self):
        if not self.images:
            messagebox.showwarning("No Images", "Please add images first")
            return
        
        fmt = self.convert_format.get()
        quality = self.convert_quality.get()
        preserve = self.preserve_convert.get()
        
        self.status_bar.config(text="Converting...")
        
        os.makedirs(self.output_dir, exist_ok=True)
        saved = 0
        
        for i, img_path in enumerate(self.images):
            try:
                img = Image.open(img_path)
                if fmt == "JPEG" and img.mode != "RGB":
                    img = img.convert("RGB")
                
                name = os.path.splitext(os.path.basename(img_path))[0]
                out_name = f"{name}_converted.{fmt.lower()}" if preserve else f"{name}.{fmt.lower()}"
                out_path = os.path.join(self.output_dir, out_name)
                
                if fmt == "JPEG":
                    img.save(out_path, fmt, quality=quality, optimize=True)
                elif fmt == "PNG":
                    img.save(out_path, fmt, compress_level=9)
                elif fmt == "WebP":
                    img.save(out_path, fmt, quality=quality)
                
                saved += 1
                progress = ((i + 1) / len(self.images)) * 100
                self.progress_bar.configure(value=progress)
                self.root.update_idletasks()
            except Exception as e:
                print(f"Error: {e}")
        
        self.progress_bar.configure(value=0)
        self.status_bar.config(text=f"Converted {saved} images to {fmt}")
        messagebox.showinfo("Complete", f"Converted {saved} images to {fmt}!\nSaved to: {self.output_dir}")
    
    def batch_process(self):
        if not self.images:
            messagebox.showwarning("No Images", "Please add images first")
            return
        
        quality = self.batch_quality.get()
        
        self.status_bar.config(text="Batch processing...")
        
        os.makedirs(self.output_dir, exist_ok=True)
        saved = 0
        
        for i, img_path in enumerate(self.images):
            try:
                img = Image.open(img_path)
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
                
                name = os.path.splitext(os.path.basename(img_path))[0]
                out_path = os.path.join(self.output_dir, f"{name}_batch.jpg")
                
                img.save(out_path, "JPEG", quality=quality, optimize=True)
                saved += 1
                
                progress = ((i + 1) / len(self.images)) * 100
                self.progress_bar.configure(value=progress)
                self.root.update_idletasks()
            except Exception as e:
                print(f"Error: {e}")
        
        self.progress_bar.configure(value=0)
        self.status_bar.config(text=f"Batch processed {saved} images")
        messagebox.showinfo("Complete", f"Batch processed {saved} images!\nSaved to: {self.output_dir}")
    
    def generate_responsive(self):
        if not self.images:
            messagebox.showwarning("No Images", "Please add an image first")
            return
        
        self.status_bar.config(text="Generating responsive images...")
        
        os.makedirs(self.output_dir, exist_ok=True)
        saved = 0
        
        sizes = [("Thumbnail", 150), ("Mobile", 320), ("Tablet", 768), 
                ("Desktop", 1280), ("Full HD", 1920)]
        
        source_img = self.images[0]
        img = Image.open(source_img)
        
        for name, size in sizes:
            if self.responsive_vars[name].get():
                try:
                    aspect = img.height / img.width
                    w = size
                    h = int(w * aspect)
                    
                    resized = img.resize((w, h), Image.Resampling.LANCZOS)
                    
                    name_base = os.path.splitext(os.path.basename(source_img))[0]
                    out_path = os.path.join(self.output_dir, f"{name_base}_{name.lower().replace(' ', '')}.jpg")
                    
                    resized.save(out_path, "JPEG", quality=85)
                    saved += 1
                except Exception as e:
                    print(f"Error: {e}")
        
        self.status_bar.config(text=f"Generated {saved} responsive images")
        messagebox.showinfo("Complete", f"Generated {saved} responsive images!\nSaved to: {self.output_dir}")
    
    def download_zip(self):
        if not self.images:
            messagebox.showwarning("No Images", "No images to download")
            return
        
        zip_path = filedialog.asksaveasfilename(defaultextension=".zip",
                                                filetypes=[("ZIP", "*.zip")])
        if zip_path:
            with zipfile.ZipFile(zip_path, 'w') as zf:
                for img in self.images:
                    zf.write(img, os.path.basename(img))
            messagebox.showinfo("Complete", f"Saved to: {zip_path}")
    
    def open_output_folder(self):
        os.makedirs(self.output_dir, exist_ok=True)
        os.startfile(self.output_dir)


def main():
    root = tk.Tk()
    app = ImageOptimizerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()