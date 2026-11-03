from __future__ import annotations

from PySide6.QtWidgets import QComboBox, QFormLayout, QFrame, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QWidget


class NewProjectPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(18)

        header = QLabel("New project")
        header.setStyleSheet("font-size: 26px; font-weight: 700; color: #E8EAED;")
        layout.addWidget(header)

        form_panel = QFrame()
        form_panel.setObjectName("panel")
        form_panel.setStyleSheet("QFrame#panel { background: #202328; border: 1px solid #383E46; border-radius: 10px; }")
        form_layout = QFormLayout(form_panel)
        form_layout.setContentsMargins(18, 18, 18, 18)
        form_layout.setSpacing(12)

        self.name_field = QLineEdit("Night Shift - Episode 04")
        self.script_field = QLineEdit("/Library/Audio/Projects/Night Shift/script.txt")
        self.audio_field = QLineEdit("/Library/Audio/Projects/Night Shift/stitched.wav")
        self.template_field = QComboBox()
        self.template_field.addItems(["Narrative Drama", "Audiobook", "Ad Break", "Podcast"])
        self.notes_field = QTextEdit("Clean room tone, maintain foreground dialogue, lift emotional swells in chapter 3.")
        self.notes_field.setFixedHeight(120)

        form_layout.addRow("Project name", self.name_field)
        form_layout.addRow("Script", self.script_field)
        form_layout.addRow("Dialogue audio", self.audio_field)
        form_layout.addRow("Template", self.template_field)
        form_layout.addRow("Production notes", self.notes_field)

        layout.addWidget(form_panel)

        actions = QHBoxLayout()
        actions.addStretch()
        primary = QPushButton("Create project")
        primary.setStyleSheet("QPushButton { background: #27C7A5; color: #111827; border: none; border-radius: 8px; padding: 10px 16px; font-weight: 600; }")
        secondary = QPushButton("Import assets")
        secondary.setStyleSheet("QPushButton { background: #262A30; color: #E8EAED; border: 1px solid #383E46; border-radius: 8px; padding: 10px 16px; }")
        actions.addWidget(secondary)
        actions.addWidget(primary)
        layout.addLayout(actions)
