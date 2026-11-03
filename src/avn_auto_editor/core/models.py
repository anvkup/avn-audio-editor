from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import List


@dataclass
class CharacterProfile:
    name: str
    voice: str
    color: str = "#27C7A5"
    script_notes: str = ""
    confidence: float = 0.0


@dataclass
class ProductionProject:
    name: str
    root: Path | str
    script_path: str | None = None
    audio_path: str | None = None
    export_path: str | None = None
    status: str = "draft"
    created_at: datetime = field(default_factory=datetime.now)
    characters: List[CharacterProfile] = field(default_factory=list)
    project_notes: str = ""

    def root_path(self) -> Path:
        return Path(self.root)


@dataclass
class PipelineResult:
    stage: str
    complete: bool
    message: str
    confidence: float = 0.0

    def as_row(self) -> tuple[str, str, str, float]:
        return (self.stage, "Complete" if self.complete else "Pending", self.message, self.confidence)
