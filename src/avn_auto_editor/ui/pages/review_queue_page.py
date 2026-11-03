from __future__ import annotations

from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout, QWidget


class ReviewQueuePage(QWidget):
    def __init__(self, pipeline=None):
        super().__init__()
        self.pipeline = pipeline
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(18)

        header = QLabel("Review queue")
        header.setStyleSheet("font-size: 26px; font-weight: 700; color: #E8EAED;")
        layout.addWidget(header)

        entries = [
            ("Cross-check VO gaps in Chapter 3", "Low confidence segment, 1.7s of missing narration"),
            ("Review room tone replacement near Intro scene", "Ambience blend may be too dense"),
            ("Confirm music cue alignment for Act II", "Music starts 0.4s before line break"),
        ]

        for title, description in entries:
            card = QFrame()
            card.setStyleSheet("QFrame { background: #202328; border: 1px solid #383E46; border-radius: 10px; }")
            box = QVBoxLayout(card)
            box.setContentsMargins(18, 16, 18, 16)
            title_label = QLabel(title)
            title_label.setStyleSheet("color: #E8EAED; font-size: 16px; font-weight: 600;")
            description_label = QLabel(description)
            description_label.setStyleSheet("color: #9299A3;")
            box.addWidget(title_label)
            box.addWidget(description_label)
            layout.addWidget(card)
