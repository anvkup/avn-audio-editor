from __future__ import annotations

from dataclasses import dataclass


@dataclass
class QAReport:
    title: str
    findings: list[str]

    def summary(self) -> str:
        return f"{self.title}: {len(self.findings)} findings"
