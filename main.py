import os
import shutil

ASSET_NAME = "picture.png"

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
output_path = os.path.join(output_dir, "entry.png")
source_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ASSET_NAME)


os.makedirs(output_dir, exist_ok=True)


shutil.copyfile(source_path, output_path)
