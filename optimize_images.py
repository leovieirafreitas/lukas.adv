import os
from PIL import Image

def optimize(filepath):
    if not os.path.exists(filepath): return
    size = os.path.getsize(filepath)
    if size > 1024 * 1024: # > 1MB
        print(f"Optimizing {filepath} ({size/1024/1024:.2f} MB)")
        try:
            img = Image.open(filepath)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            
            # resize if too large
            if img.width > 1920:
                ratio = 1920.0 / img.width
                img = img.resize((1920, int(img.height * ratio)), Image.Resampling.LANCZOS)
                
            out_path = filepath.rsplit(".", 1)[0] + ".webp"
            img.save(out_path, "WEBP", quality=80)
            print(f"Saved {out_path}")
        except Exception as e:
            print(f"Failed {filepath}: {e}")

assets_dir = r"c:\Users\FELIPE BARROSO\Documents\LUKAS_ADV\assets"
for f in os.listdir(assets_dir):
    if f.lower().endswith((".png", ".jpg", ".jpeg")):
        optimize(os.path.join(assets_dir, f))
