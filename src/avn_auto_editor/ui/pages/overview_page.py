from __future__ import annotations

from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QVBoxLayout, QWidget


class OverviewPage(QWidget):
    def __init__(self, pipeline=None):
        super().__init__()
        self.pipeline = pipeline
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(18)

        header = QLabel("Overview")
        header.setStyleSheet("font-size: 26px; font-weight: 700; color: #E8EAED;")
        layout.addWidget(header)

        summary_row = QHBoxLayout()
        summary_row.addWidget(self._stat_card("Projects", "18"))
        summary_row.addWidget(self._stat_card("Auto QA", "94%"))
        summary_row.addWidget(self._stat_card("SFX matches", "328"))
        summary_row.addWidget(self._stat_card("Ready for review", "7"))
        layout.addLayout(summary_row)

        body = QHBoxLayout()
        body.addWidget(self._list_panel())
        body.addWidget(self._activity_panel())
        layout.addLayout(body)

    def _stat_card(self, label: str, value: str) -> QWidget:
        widget = QFrame()
        widget.setObjectName("panel")
        widget.setStyleSheet("QFrame#panel { background: #202328; border: 1px solid #383E46; border-radius: 10px; }")
        box = QVBoxLayout(widget)
        box.setContentsMargins(18, 14, 18, 14)
        title = QLabel(label)
        title.setStyleSheet("color: #9299A3; font-size: 12px; text-transform: uppercase; letter-spacing: 0.08em;")
        amount = QLabel(value)
        amount.setStyleSheet("color: #E8EAED; font-size: 26px; font-weight: 700;")
        box.addWidget(title)
        box.addWidget(amount)
        return widget

    def _list_panel(self) -> QWidget:
        panel = QFrame()
        panel.setObjectName("panel")
        panel.setStyleSheet("QFrame#panel { background: #202328; border: 1px solid #383E46; border-radius: 10px; }")
        box = QVBoxLayout(panel)
        box.setContentsMargins(18, 18, 18, 18)
        title = QLabel("Current workload")
        title.setStyleSheet("color: #E8EAED; font-size: 16px; font-weight: 600;")
        box.addWidget(title)

        items = [
            ("Lumen House", "Character matching complete", "Ready"),
            ("The Last Broadcast", "SFX curation in progress", "Processing"),
            ("Night Shift", "Dialogue pickup review", "Review"),
        ]

        for project_name, status_text, state in items:
            row = QFrame()
            row.setStyleSheet("QFrame { background: #262A30; border: 1px solid #383E46; border-radius: 8px; }")
            row_layout = QHBoxLayout(row)
            row_layout.setContentsMargins(12, 10, 12, 10)
            project = QLabel(project_name)
            project.setStyleSheet("color: #E8EAED; font-weight: 600;")
            info = QLabel(status_text)
            info.setStyleSheet("color: #9299A3;")
            badge = QLabel(state)
            badge.setStyleSheet("color: #27C7A5; background: rgba(39, 199, 165, 0.12); border-radius: 6px; padding: 4px 8px; font-size: 11px;")
            row_layout.addWidget(project)
            row_layout.addWidget(info)
            row_layout.addWidget(badge)
            box.addWidget(row)

        return panel

    def _activity_panel(self) -> QWidget:
        panel = QFrame()
        panel.setObjectName("panel")
        panel.setStyleSheet("QFrame#panel { background: #202328; border: 1px solid #383E46; border-radius: 10px; }")
        box = QVBoxLayout(panel)
        box.setContentsMargins(18, 18, 18, 18)
        title = QLabel("Automation status")
        title.setStyleSheet("color: #E8EAED; font-size: 16px; font-weight: 600;")
        box.addWidget(title)

        if self.pipeline is not None:
            for stage in self.pipeline.stages[:4]:
                item = QFrame()
                item.setStyleSheet("QFrame { background: #262A30; border: 1px solid #383E46; border-radius: 8px; }")
                il = QHBoxLayout(item)
                il.setContentsMargins(12, 10, 12, 10)
                name = QLabel(stage.stage)
                name.setStyleSheet("color: #E8EAED;")
                state = QLabel("Complete" if stage.complete else "Pending")
                state.setStyleSheet(
                    "color: #27C7A5;" if stage.complete else "color: #E5B45C;"
                )
                il.addWidget(name)
                il.addWidget(state)
                box.addWidget(item)

        return panel
