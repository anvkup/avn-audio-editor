from __future__ import annotations


class DuckingEngine:
    def duck(self, music_level_db: float) -> float:
        return max(music_level_db - 6.0, -24.0)
