from __future__ import annotations

from PySide6.QtWidgets import QCheckBox, QFrame, QFormLayout, QLabel, QVBoxLayout, QWidget


class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(18)

        header = QLabel("Settings")
        header.setStyleSheet("font-size: 26px; font-weight: 700; color: #E8EAED;")
        layout.addWidget(header)

        panel = QFrame()
        panel.setStyleSheet("QFrame { background: #202328; border: 1px solid #383E46; border-radius: 10px; }")
        form = QFormLayout(panel)
        form.setContentsMargins(18, 18, 18, 18)
        form.setSpacing(12)

        toggles = [
            ("Auto transcription", True),
            ("Speaker matching", True),
            ("Sound recommendations", True),
            ("Music recommendations", True),
            ("Auto mixing", True),
            ("Generate REAPER project", True),
            ("Run QA automatically", False),
        ]

        for label, checked in toggles:
            box = QCheckBox(label)
            box.setChecked(checked)
            box.setStyleSheet("QCheckBox { color: #E8EAED; }")
            form.addRow(box)

        layout.addWidget(panel)
