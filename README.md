# mdView

A Python web app that opens local `.md` files and renders them with clean formatting.

## MVP features

- Open local Markdown using file upload
- Open local Markdown by entering file path
- Proper Markdown rendering for headings, lists, tables, blockquotes, and fenced code
- Light/Dark theme toggle with persistence in browser local storage
- Cross-platform run instructions (Linux, Windows, macOS)

## Screenshots

### Viewer UI

![mdView viewer](screenshot_20260508_114341.jpg)

### Rendered view

![mdView alternate view](screenshot_20260508_115031.jpg)

## Quick start

### 1) Create and activate virtual environment

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

### 3) Run the app

```bash
python run.py
```

Then open `http://127.0.0.1:5000` in your browser.

## Run tests

```bash
pytest -q
```

## Project layout

```text
app/
  __init__.py
  routes.py
  markdown_utils.py
  templates/
  static/
run.py
tests/
samples/
```

## Notes

- Only `.md` files are accepted.
- Files are expected to be UTF-8 encoded.
- HTML output is sanitized before rendering.
