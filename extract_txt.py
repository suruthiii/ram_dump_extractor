import os
import zipfile
import subprocess

input_folder = "dump files"
extracted_images_folder = "extracted images"
output_txt_folder = "extracted txt files"

os.makedirs(extracted_images_folder, exist_ok=True)
os.makedirs(output_txt_folder, exist_ok=True)

def extract_zips():
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".zip"):
            zip_path = os.path.join(input_folder, filename)
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                for member in zip_ref.namelist():
                    if member.lower().endswith(('.raw', '.mem', '.img', '.bin', '.mddramimage')):
                        extracted_path = os.path.join(extracted_images_folder, os.path.basename(member))
                        with zip_ref.open(member) as source, open(extracted_path, 'wb') as target:
                            target.write(source.read())
                        break

def convert_to_txt(image_path):
    vol_script = os.path.abspath("../vol.py")
    python_path = "python"
    plugin = "windows.pslist"
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    output_file = os.path.join(output_txt_folder, f"pslist_{base_name}.txt")
    command = [python_path, vol_script, "-f", image_path, plugin]
    with open(output_file, "w", encoding="utf-16") as f:
        subprocess.run(command, stdout=f)
    return output_file

def process_images():
    for folder in [input_folder, extracted_images_folder]:
        for filename in os.listdir(folder):
            if filename.lower().endswith(('.raw', '.mem', '.img', '.bin', '.mddramimage')):
                image_path = os.path.join(folder, filename)
                output_file = convert_to_txt(image_path)
                print(f"[✓] Generated {output_file}")

def main():
    extract_zips()
    process_images()

if __name__ == "__main__":
    main()