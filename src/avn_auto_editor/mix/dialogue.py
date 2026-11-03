from __future__ import annotations


class DialogueMixEngine:
    def process(self, track_name: str) -> dict[str, float]:
        return {"gain_db": -1.2, "eq": 2.5}
