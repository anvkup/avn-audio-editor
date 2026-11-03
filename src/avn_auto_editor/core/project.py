from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path


@dataclass
class ProjectSession:
    name: str
    root: str | Path
    script_path: str | None = None
    audio_path: str | None = None
    status: str = "draft"
    created_at: datetime = field(default_factory=datetime.now)
    notes: str = ""

    def root_path(self) -> Path:
        return Path(self.root)

    def is_ready(self) -> bool:
        return bool(self.script_path and self.audio_path)
