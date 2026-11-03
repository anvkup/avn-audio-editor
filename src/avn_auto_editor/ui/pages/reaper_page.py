from __future__ import annotations

from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout, QWidget


class ReaperPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(18)

        header = QLabel("REAPER")
        header.setStyleSheet("font-size: 26px; font-weight: 700; color: #E8EAED;")
        layout.addWidget(header)

        card = QFrame()
        card.setStyleSheet("QFrame { background: #202328; border: 1px solid #383E46; border-radius: 10px; }")
        box = QVBoxLayout(card)
        box.setContentsMargins(20, 20, 20, 20)
        title = QLabel("Project export")
        title.setStyleSheet("color: #E8EAED; font-size: 18px; font-weight: 600;")
        info = QLabel("Template: Dramatic Narration 24-bit 48k • Tracks: 14 • Bounces: 3 • Under review: 0")
        info.setStyleSheet("color: #9299A3;")
        box.addWidget(title)
        box.addWidget(info)
        layout.addWidget(card)
