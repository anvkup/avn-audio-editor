from __future__ import annotations

import sys

from PySide6.QtWidgets import QApplication

from avn_auto_editor.ui.main_window import MainWindow


def create_application() -> QApplication:
    app = QApplication(sys.argv)
    app.setApplicationName("AVN Auto Editor")
    app.setOrganizationName("AVN")
    return app


def run() -> int:
    app = create_application()
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(run())
