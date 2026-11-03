from __future__ import annotations

from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout, QWidget


class SoundLibraryPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(18)

        header = QLabel("Sound library")
        header.setStyleSheet("font-size: 26px; font-weight: 700; color: #E8EAED;")
        layout.addWidget(header)

        for category, value in [
            ("SFX library", "1,284 samples"),
            ("Ambience library", "436 loops"),
            ("Music beds", "92 cue packs"),
            ("Character-specific layers", "17 profiles"),
        ]:
            card = QFrame()
            card.setStyleSheet("QFrame { background: #202328; border: 1px solid #383E46; border-radius: 10px; }")
            box = QVBoxLayout(card)
            box.setContentsMargins(18, 16, 18, 16)
            title = QLabel(category)
            title.setStyleSheet("color: #E8EAED; font-size: 16px; font-weight: 600;")
            detail = QLabel(value)
            detail.setStyleSheet("color: #9299A3;")
            box.addWidget(title)
            box.addWidget(detail)
            layout.addWidget(card)
