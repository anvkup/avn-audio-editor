from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Segment:
    start: float
    end: float
    label: str = "segment"


class Segmenter:
    def segment(self, transcript: list) -> list[Segment]:
        return [Segment(0.0, 1.0, "intro")]
