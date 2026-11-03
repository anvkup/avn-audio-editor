from __future__ import annotations

from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QVBoxLayout, QWidget


class CharactersPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(18)

        header = QLabel("Characters")
        header.setStyleSheet("font-size: 26px; font-weight: 700; color: #E8EAED;")
        layout.addWidget(header)

        for name, voice, role in [
            ("Maya Rivers", "Warm intimate baritone", "Lead narrator"),
            ("Cole Mercer", "Focused dramatic tenor", "Antagonist"),
            ("Nia Hollow", "Bright arresting soprano", "Witness"),
            ("Jasper Vale", "Low grounded bass", "Supporting character"),
        ]:
            card = QFrame()
            card.setStyleSheet("QFrame { background: #202328; border: 1px solid #383E46; border-radius: 10px; }")
            box = QVBoxLayout(card)
            box.setContentsMargins(18, 16, 18, 16)
            row = QHBoxLayout()
            badge = QLabel()
            badge.setStyleSheet("background: #27C7A5; border-radius: 12px; min-width: 24px; min-height: 24px;")
            name_label = QLabel(name)
            name_label.setStyleSheet("color: #E8EAED; font-size: 18px; font-weight: 600;")
            row.addWidget(badge)
            row.addWidget(name_label)
            box.addLayout(row)
            box.addWidget(QLabel(f"Voice profile: {voice}"))
            box.addWidget(QLabel(f"Role: {role}"))
            layout.addWidget(card)
