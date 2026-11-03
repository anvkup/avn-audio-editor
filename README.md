# AVN Auto Editor

AVN Auto Editor is a desktop application for AI-assisted audio post-production. It is designed for audiobook, scripted drama, episodic storytelling, and production-heavy voice workflows where the user needs to import a stitched dialogue recording and a production script, then automate the editing pipeline from transcription through REAPER export.

## Features

- Dark workstation-inspired interface built with PySide6
- Project dashboard and workflow navigation
- Script, audio, transcription, and character tracking
- Modular architecture for future automation stages
- REAPER-export-focused project generation workflow
- QA review queue for questionable or uncertain edits

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Project layout

```text
avn-audio-editor/
├── app.py
├── requirements.txt
├── pyproject.toml
├── README.md
├── src/
│   └── avn_auto_editor/
│       ├── __init__.py
│       ├── main.py
│       ├── core/
│       ├── ui/
│       └── ...
└── tests/
```

## Status

This is the initial professional application scaffold with a working PySide6 shell and structured workflow modules that fit the AVN Auto Editor product direction.
