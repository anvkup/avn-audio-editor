from __future__ import annotations

from pathlib import Path


class ReaperExporter:
    def export(self, project_root: str, project_name: str) -> Path:
        target = Path(project_root) / f"{project_name}.RPP"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("REAPER project placeholder\n", encoding="utf-8")
        return target
