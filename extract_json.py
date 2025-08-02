import os
import json

input_folder = "extracted txt files"
output_folder = "extracted json files"

os.makedirs(output_folder, exist_ok=True)

def parse_pslist(lines):
    events = []
    header_found = False
    for line in lines:
        if not line.strip() or line.startswith("Volatility"):
            continue
        if "PID" in line and "PPID" in line and "ImageFileName" in line:
            header_found = True
            continue
        if not header_found:
            continue
        parts = line.strip().split('\t')
        if len(parts) < 9:
            continue
        pid = parts[0]
        ppid = parts[1]
        image = parts[2]
        create_time = parts[8]
        if create_time == "N/A":
            continue
        timestamp = create_time.replace(" ", "T").replace(" UTC", "Z")
        events.append({
            "event": "Process_Start",
            "actor": f"{image} (PID:{pid})",
            "target": "SYSTEM",
            "location": "RAM",
            "timestamp": timestamp,
            "source": "Volatility3",
            "sequence_id": f"PROC-{pid}",
            "causal_context": f"Parent_PID:{ppid}",
            "data_dependencies": [image]
        })
    return events

def process_file(filepath):
    filename = os.path.basename(filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    if filename.lower().startswith("pslist"):
        return parse_pslist(lines)
    return []

def main():
    for file in os.listdir(input_folder):
        if file.lower().endswith(".txt"):
            input_path = os.path.join(input_folder, file)
            events = process_file(input_path)
            if events:
                output_filename = file.replace(".txt", "_events.json")
                output_path = os.path.join(output_folder, output_filename)
                with open(output_path, "w", encoding="utf-8") as f:
                    json.dump(events, f, indent=2)
                print(f"[✓] Extracted {len(events)} events from {file} → {output_filename}")
            else:
                print(f"[ ] Skipped {file} (no parser or no valid events)")

if __name__ == "__main__":
    main()