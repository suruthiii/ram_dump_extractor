# Memory Analysis Workflow

This repository contains scripts to extract process information from memory dumps using Volatility 3 and convert the output into structured JSON (CASE Standard) events.

---

## 🔄 Workflow Overview

1. **Extract text data** from memory dumps using Volatility (`extract_txt.py`)
2. **Convert text output** to JSON events (`extract_json.py`)

---

## 🚀 Getting Started

### 📦 Prerequisites

- Python 3.6+
- [Volatility 3](https://github.com/volatilityfoundation/volatility3) cloned and set up

---

### ⚙️ Setup

First, clone Volatility 3:

```bash
git clone https://github.com/volatilityfoundation/volatility3.git
```

Then, **clone this repository inside the Volatility 3 directory**:

```bash
cd volatility3
git clone https://github.com/yourusername/memory-analysis-workflow.git
cd memory-analysis-workflow
```

---

## 🧪 Running the Analysis

Place your memory dump files in the `dump files/` directory.

### 1. Generate text files from memory dumps:

```bash
python extract_txt.py
```

### 2. Convert text files to JSON events:

```bash
python extract_json.py
```

---

## 🗂️ Folder Structure

```
📁 volatility3/
├── 📄 vol.py                          
├── ...
├── ...
├── 📁 memory-analysis-workflow/       
│   ├── 📁 dump files/                 
│   │   ├── 📄 charlie-2009-11-16.mddramimage.zip
│   │   └── 📄 charlie-2009-11-17.mddramimage.zip
│   │
│   ├── 📁 extracted images/           
│   │   ├── 📄 charlie-2009-11-16.mddramimage
│   │   └── 📄 charlie-2009-11-17.mddramimage
│   │
│   ├── 📁 extracted txt files/        
│   │   ├── 📄 pslist_charlie-2009-11-16.txt
│   │   └── 📄 pslist_charlie-2009-11-17.txt
│   │
│   ├── 📁 extracted json files/       
│   │   ├── 📄 pslist_charlie-2009-11-16_events.json
│   │   └── 📄 pslist_charlie-2009-11-17_events.json
│   │
│   ├── 📄 .gitignore
│   ├── 📄 extract_json.py             
│   ├── 📄 extract_txt.py              
│   └── 📄 README.md                   
```

---

## 📄 File Descriptions

### 🔧 Scripts

- **extract_txt.py** – Processes memory dump files (RAW, MEM, IMG, BIN, MDDRAMIMAGE) and ZIP archives containing them.
- **extract_json.py** – Converts Volatility pslist output to JSON event format.

### 📥 Input Files

- `dump files/*.zip` – Compressed memory dump files
- `dump files/*.mddramimage` – Raw memory dump files

### 📤 Output Files

- `extracted txt files/pslist_*.txt` – Tab-separated process lists from Volatility
- `extracted json files/*_events.json` – Structured process start events in JSON format

---

## 📌 Output Example

```json
[
  {
    "event": "Process_Start",
    "actor": "smss.exe (PID:824)",
    "target": "SYSTEM",
    "location": "RAM",
    "timestamp": "2009-11-17T02:27:39.000000Z",
    "source": "Volatility3",
    "sequence_id": "PROC-824",
    "causal_context": "Parent_PID:4",
    "data_dependencies": ["smss.exe"]
  },
  {
    "event": "Process_Start",
    "actor": "explorer.exe (PID:476)",
    "target": "SYSTEM",
    "location": "RAM",
    "timestamp": "2009-11-17T02:27:51.000000Z",
    "source": "Volatility3",
    "sequence_id": "PROC-476",
    "causal_context": "Parent_PID:944",
    "data_dependencies": ["explorer.exe"]
  }
]
```

---

## 🛠️ Support

For support or feature requests, please open an issue on GitHub.

---

## ✅ This README includes:

1. **Visual Folder Structure** with emoji icons for better readability  
2. **Clear Step-by-Step Instructions** for running the scripts  
3. **File Type Descriptions** for all input and output files  
4. **Comprehensive Workflow Explanation** showing the data processing pipeline  
5. **Realistic JSON Example** with multiple process entries  
6. **Directory Path Formatting** using `📁` and `📄` emojis for visual distinction  
7. **Prerequisites Section** with link to Volatility 3  
8. **Support Information** for issue reporting  

---

📦 The structure shows:

- ZIP files in `dump files/`  
- Extracted images in `extracted images/`  
- Volatility outputs in `extracted txt files/`  
- Final JSON in `extracted json files/`  
- Script files in root directory inside Volatility 3  

📚 The emoji-enhanced tree view makes it easy to visualize the repository organization at a glance.
