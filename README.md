# Keyword Extraction Tool

A simple Streamlit web app that extracts keywords from a block of text.
The app tries to use the legacy `gensim.summarization.keywords` when available
and falls back to YAKE (a pure-Python keyword extractor) on modern Python.

This repository contains:

- `KeywordExtraction.py` — the Streamlit app entrypoint (contains `extract_keywords(text)` and `main()`).
- `requirements.txt` — Python dependencies (Streamlit + YAKE).

---

## Prerequisites

- Python 3.8+ is recommended. The app works on modern Python (3.10/3.11/3.12/3.13) with the YAKE fallback.
- A virtual environment is strongly recommended to avoid polluting your global Python installation.

---

## Setup (PowerShell)

1. Open PowerShell in the project folder (where `KeywordExtraction.py` and `requirements.txt` live).

2. (Optional but recommended) If you don't have a virtual environment yet, create one:

```powershell
py -3 -m venv .venv
```

3. Install dependencies. There are two safe options depending on whether you want to activate the venv or call the venv python directly.

Option A — use the venv Python directly (works even if Activate.ps1 is restricted):

```powershell
# Upgrade pip inside the venv and install requirements
& .\\.venv\\Scripts\\python.exe -m pip install --upgrade pip
& .\\.venv\\Scripts\\python.exe -m pip install -r .\\requirements.txt

# Run the app
& .\\.venv\\Scripts\\python.exe -m streamlit run .\\KeywordExtraction.py
```

Option B — activate the venv then install and run (PowerShell activation):

```powershell
# Activate the virtual environment (PowerShell)
.\\.venv\\Scripts\\Activate.ps1

# Then inside the activated venv
pip install --upgrade pip
pip install -r .\\requirements.txt
streamlit run .\\KeywordExtraction.py
```

If `Activate.ps1` is blocked by your system execution policy, use Option A instead.

Option C — install into your user Python (no venv):

```powershell
py -3 -m pip install --user --upgrade pip
py -3 -m pip install --user -r .\\requirements.txt
py -3 -m streamlit run .\\KeywordExtraction.py
```

---

## How to use the app

1. The Streamlit UI will open in your browser (or show a local URL in the terminal).
2. Paste or type the text you want to analyze into the text area.
3. Click the `Extract Keywords` button.
4. The app will display extracted keywords in a bullet list and a comma-separated line.

Notes:
- If the legacy `gensim.summarization` module is installed and available, the app will use it (keeps original behavior).
- If `gensim.summarization` is not available (common on new Python versions), the app uses YAKE automatically.

---

## Troubleshooting

- "No module named streamlit" — make sure you installed the requirements into the same Python environment you are running Streamlit from (use the venv python or activate the venv).
- If you specifically need `gensim.summarization` (older gensim), create a venv with an older Python (e.g., 3.8 or 3.9) and install `gensim==3.8.3` there; note this may require building wheels and additional system dependencies.
- If you see permission/execution policy errors when activating the venv in PowerShell, use the venv python directly (Option A above) or run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` for the session.

---

If you'd like, I can add a small `run.ps1` script that runs the safe Option A commands for you. Just ask and I'll add it.

Happy keywording! 🎯
