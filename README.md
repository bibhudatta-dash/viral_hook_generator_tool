# 🚀 High-Retention Viral Hook & Chapter Generator

A lightweight, localized Python backend engine built to optimize short-form video workflow pipelines. This utility scans media transcript logs line-by-line, runs conditional keyword parsing against multi-category psychological retention filters, and extracts ready-to-use video hooks and timestamps into clean social-ready assets.

---

## 🔒 Security & Performance Features
* **100% Local Execution:** The tool processes data entirely in local memory stream loops. It requires zero network connectivity, zero browser token collection, and zero administrative access.
* **Bilingual Multi-Script Processing:** Fully optimized with universal `UTF-8` encoding to process English, Hinglish, and Hindi (Devnagari script) text flawlessly without system environment crashes.
* **High Efficiency Engine:** Utilizes sequential line iteration streaming to handle large production multi-gigabyte log data using near-zero RAM footprint.

---

## 🛠️ How It Works Under The Hood
1. **Ingestion:** Opens a raw layout file (`transcript.txt`) using dynamic context managers.
2. **Analysis:** Runs nested evaluation conditions (`if/else`) utilizing structural keyword dictionaries (`Curiosity Hooks`, `Value Promises`, `Action Triggers`).
3. **Data Transformation:** Isolates core content text using string array mutations (`.split()`) and appends clean data arrays to final extraction targets.
4. **Export:** Automatically generates an organized standalone document (`export_hooks.txt`).

---

## 💻 Manual Local Execution
If you prefer executing the raw source logic natively rather than utilizing a pre-compiled binary package:

1. Clone this repository to your system workspace.
2. Drop your raw subtitle file into the directory and save it as `transcript.txt`.
3. Open your terminal console inside the path and execute:
   ```bash
   python generator.py
   ```
