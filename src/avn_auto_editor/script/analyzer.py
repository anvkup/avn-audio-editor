from __future__ import annotations


class ScriptAnalyzer:
    def analyze(self, lines: list) -> dict[str, object]:
        return {"dialogue_count": len(lines), "characters": sorted({line.character for line in lines if line.character})}
