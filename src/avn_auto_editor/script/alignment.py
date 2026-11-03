from __future__ import annotations


class AlignmentEngine:
    def align(self, script_lines: list, transcript: list) -> list:
        return list(zip(script_lines, transcript))
