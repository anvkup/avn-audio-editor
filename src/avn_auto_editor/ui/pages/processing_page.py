from __future__ import annotations

from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget


class ProcessingPage(QWidget):
    def __init__(self, pipeline=None):
        super().__init__()
        self.pipeline = pipeline
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(18)

        header = QLabel("Processing")
        header.setStyleSheet("font-size: 26px; font-weight: 700; color: #E8EAED;")
        layout.addWidget(header)

        table = QTableWidget(0, 4)
        table.setHorizontalHeaderLabels(["Stage", "Status", "Details", "Confidence"])
        table.setAlternatingRowColors(True)
        table.setStyleSheet(
            "QTableWidget { background: #202328; color: #E8EAED; border: 1px solid #383E46; gridline-color: #383E46; }"
            "QHeaderView::section { background: #262A30; color: #E8EAED; padding: 8px; border: 1px solid #383E46; }"
        )

        if self.pipeline is not None:
            table.setRowCount(len(self.pipeline.stages))
            for row_index, stage in enumerate(self.pipeline.stages):
                table.setItem(row_index, 0, QTableWidgetItem(stage.stage))
                table.setItem(row_index, 1, QTableWidgetItem("Complete" if stage.complete else "Pending"))
                table.setItem(row_index, 2, QTableWidgetItem(stage.message))
                table.setItem(row_index, 3, QTableWidgetItem(f"{stage.confidence:.2f}"))
        else:
            table.setRowCount(1)
            table.setItem(0, 0, QTableWidgetItem("No pipeline running"))
            table.setItem(0, 1, QTableWidgetItem("Idle"))
            table.setItem(0, 2, QTableWidgetItem("Load a project to begin orchestration."))
            table.setItem(0, 3, QTableWidgetItem("0.00"))

        table.resizeColumnsToContents()
        layout.addWidget(table)

        summary = QFrame()
        summary.setStyleSheet("QFrame { background: #202328; border: 1px solid #383E46; border-radius: 10px; }")
        summary_layout = QHBoxLayout(summary)
        summary_layout.setContentsMargins(18, 18, 18, 18)
        if self.pipeline is not None:
            total = self.pipeline.summary()
            summary_layout.addWidget(QLabel(f"Completion: {total['completion']}%"))
            summary_layout.addWidget(QLabel(f"Average confidence: {total['average_confidence']:.2f}"))
        else:
            summary_layout.addWidget(QLabel("Completion: 0%"))
            summary_layout.addWidget(QLabel("Average confidence: 0.00"))
        layout.addWidget(summary)
