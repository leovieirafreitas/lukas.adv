import sys
import subprocess
import shutil
import os

# Install required packages if not present
try:
    from PIL import Image
    import pillow_heif
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pillow', 'pillow-heif'])
    from PIL import Image
    import pillow_heif

pillow_heif.register_heif_opener()

base_dir = r"c:\Users\FELIPE BARROSO\Documents\LUKAS_ADV"
logo_dir = os.path.join(base_dir, "logo")
assets_dir = os.path.join(base_dir, "assets")

# Convert HEIC to JPG
heic_path = os.path.join(logo_dir, "IMG_0212.HEIC")
if os.path.exists(heic_path):
    img = Image.open(heic_path)
    img.save(os.path.join(assets_dir, "person1.jpg"))

# Copy person 2
p2_src = os.path.join(logo_dir, "76023664-3206-4DC7-AD70-B39AEC60BC1D.JPG.jpeg")
if os.path.exists(p2_src):
    shutil.copy(p2_src, os.path.join(assets_dir, "person2.jpg"))

# Copy bg
bg_src = os.path.join(logo_dir, "Default_bookshelf_with_books_in_a_highly_realistic_law_office_1 Palette.png")
if os.path.exists(bg_src):
    shutil.copy(bg_src, os.path.join(assets_dir, "hero-bg.png"))

print("Images prepared.")
