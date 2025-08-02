import subprocess
import os

vol_script = os.path.abspath("../vol.py") 
python_path = "python" 

image_path = os.path.join("dump files", "pat-2009-11-17.mddramimage")
output_folder = os.path.join("extracted files")
output_file = os.path.join(output_folder, "pslist.txt")

os.makedirs(output_folder, exist_ok=True)

plugin = "windows.pslist"

command = [
    python_path,
    vol_script,
    "-f", image_path,
    plugin
]

with open(output_file, "w", encoding="utf-16") as f:
    subprocess.run(command, stdout=f)

print(f"[✓] Saved '{plugin}' output to {output_file}")
