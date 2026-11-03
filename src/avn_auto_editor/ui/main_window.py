from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QButtonGroup,
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from avn_auto_editor.core.models import ProductionProject
from avn_auto_editor.core.pipeline import ProcessingPipeline
from avn_auto_editor.ui.pages.characters_page import CharactersPage
from avn_auto_editor.ui.pages.processing_page import ProcessingPage
from avn_auto_editor.ui.pages.project_page import NewProjectPage
from avn_auto_editor.ui.pages.projects_page import ProjectsPage
from avn_auto_editor.ui.pages.reaper_page import ReaperPage
from avn_auto_editor.ui.pages.review_queue_page import ReviewQueuePage
from avn_auto_editor.ui.pages.settings_page import SettingsPage
from avn_auto_editor.ui.pages.sound_library_page import SoundLibraryPage
from avn_auto_editor.ui.pages.overview_page import OverviewPage

APP_STYLE = """
QMainWindow {
    background: #17191C;
    color: #E8EAED;
}

QWidget {
    background: #17191C;
    color: #E8EAED;
    font-family: "SF Pro Display", "Segoe UI", sans-serif;
}

QPushButton {
    border: 1px solid #383E46;
    border-radius: 8px;
    padding: 8px 12px;
    background: #202328;
    color: #E8EAED;
}

QPushButton:hover {
    background: #262A30;
}

QPushButton:checked {
    background: #27C7A5;
    color: #17191C;
    border: 1px solid rgba(39, 199, 165, 0.7);
}

QScrollArea {
    border: none;
}

QLabel {
    color: #E8EAED;
}
"""

NAV_ITEMS = [
    ("Overview", "overview"),
    ("New Project", "new_project"),
    ("Projects", "projects"),
    ("Processing", "processing"),
    ("Review Queue", "review_queue"),
    ("Characters", "characters"),
    ("Sound Library", "sound_library"),
    ("REAPER", "reaper"),
    ("Settings", "settings"),
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AVN Auto Editor")
        self.resize(1480, 920)
        self.setStyleSheet(APP_STYLE)

        self.project = ProductionProject(name="Night Shift - Episode 04", root="/Users/anvkup/Documents/Projects/Night Shift")
        self.pipeline = ProcessingPipeline(self.project)

        self._build_ui()

    def _build_ui(self):
        root = QWidget(self)
        root_layout = QHBoxLayout(root)
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(0)

        sidebar = QFrame()
        sidebar.setObjectName("sidebar")
        sidebar.setStyleSheet(
            "QFrame#sidebar { background: #202328; border-right: 1px solid #383E46; min-width: 220px; max-width: 220px; }"
        )
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(16, 18, 16, 16)
        sidebar_layout.setSpacing(10)

        logo = QLabel("AVN")
        logo.setStyleSheet("font-size: 18px; font-weight: 700; color: #E8EAED; letter-spacing: 0.22em; padding: 8px 0 18px 0;")
        sidebar_layout.addWidget(logo)

        nav_group = QButtonGroup(self)
        nav_group.setExclusive(True)

        for title, key in NAV_ITEMS:
            button = QPushButton(title)
            button.setCheckable(True)
            button.setObjectName(key)
            button.setCursor(Qt.PointingHandCursor)
            button.setStyleSheet(
                "QPushButton { text-align: left; padding: 10px 12px; border-radius: 8px; border: 1px solid transparent; background: transparent; }"
                "QPushButton:checked { background: #27C7A5; color: #17191C; border: 1px solid rgba(39, 199, 165, 0.9); }"
            )
            nav_group.addButton(button)
            sidebar_layout.addWidget(button)
            button.clicked.connect(lambda checked, k=key: self.show_page(k))

        sidebar_layout.addStretch()
        status = QLabel("Production ready")
        status.setStyleSheet("color: #54B88A; font-size: 11px; letter-spacing: 0.08em; text-transform: uppercase;")
        sidebar_layout.addWidget(status)

        content = QWidget()
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(0, 0, 0, 0)
        self.stack = QStackedWidget()
        self.stack.addWidget(OverviewPage(self.pipeline))
        self.stack.addWidget(NewProjectPage())
        self.stack.addWidget(ProjectsPage())
        self.stack.addWidget(ProcessingPage(self.pipeline))
        self.stack.addWidget(ReviewQueuePage(self.pipeline))
        self.stack.addWidget(CharactersPage())
        self.stack.addWidget(SoundLibraryPage())
        self.stack.addWidget(ReaperPage())
        self.stack.addWidget(SettingsPage())
        content_layout.addWidget(self.stack)

        root_layout.addWidget(sidebar)
        root_layout.addWidget(content)
        self.setCentralWidget(root)

        self.show_page("overview")

    def show_page(self, key: str) -> None:
        index = {
            "overview": 0,
            "new_project": 1,
            "projects": 2,
            "processing": 3,
            "review_queue": 4,
            "characters": 5,
            "sound_library": 6,
            "reaper": 7,
            "settings": 8,
        }.get(key, 0)
        self.stack.setCurrentIndex(index)

        for button in self.centralWidget().findChildren(QPushButton):
            if button.objectName() == key:
                button.setChecked(True)
