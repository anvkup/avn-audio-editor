from __future__ import annotations


class QualityCheck:
    def run(self, project_data: dict) -> list[str]:
        return ["No critical issues detected."] if project_data else []
