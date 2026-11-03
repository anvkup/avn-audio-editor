from __future__ import annotations

from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QVBoxLayout, QWidget


class ProjectsPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(18)

        header = QLabel("Projects")
        header.setStyleSheet("font-size: 26px; font-weight: 700; color: #E8EAED;")
        layout.addWidget(header)

        for project_name, status, progress in [
            ("Lumen House", "Ready for mix", "92%"),
            ("The Last Broadcast", "QA review", "76%"),
            ("Night Shift", "In progress", "61%"),
            ("Glass Harbor", "Asset import", "29%"),
        ]:
            card = QFrame()
            card.setStyleSheet("QFrame { background: #202328; border: 1px solid #383E46; border-radius: 10px; }")
            box = QVBoxLayout(card)
            box.setContentsMargins(18, 16, 18, 16)
            row = QHBoxLayout()
            name = QLabel(project_name)
            name.setStyleSheet("color: #E8EAED; font-size: 18px; font-weight: 600;")
            badge = QLabel(status)
            badge.setStyleSheet("color: #27C7A5; background: rgba(39, 199, 165, 0.12); border-radius: 6px; padding: 4px 8px; font-size: 11px;")
            row.addWidget(name)
            row.addStretch()
            row.addWidget(badge)
            box.addLayout(row)
            meta = QLabel(f"Completion: {progress} • Script: 226 lines • Audio: 41 mins")
            meta.setStyleSheet("color: #9299A3;")
            box.addWidget(meta)
            layout.addWidget(card)
