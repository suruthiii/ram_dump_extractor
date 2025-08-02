import subprocess
import os

vol_script = os.path.abspath("../vol.py")
python_path = "python"
plugin = "windows.pslist"

input_folder = os.path.join("dump files")
output_folder = os.path.join("extracted files")
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".raw", ".mem", ".img", ".bin", ".mddramimage")):
        image_path = os.path.join(input_folder, filename)
        base_name = os.path.splitext(filename)[0]
        output_file = os.path.join(output_folder, f"pslist_{base_name}.txt")
        command = [
            python_path,
            vol_script,
            "-f", image_path,
            plugin
        ]
        with open(output_file, "w", encoding="utf-16") as f:
            subprocess.run(command, stdout=f)
        print(f"[✓] Saved '{plugin}' output to {output_file}")
