from __future__ import annotations

from dataclasses import dataclass


@dataclass
class SpeakerTurn:
    speaker_id: str
    start: float
    end: float
    confidence: float


class SpeakerDiarizer:
    def diarize(self, transcript: list) -> list[SpeakerTurn]:
        return [SpeakerTurn("speaker-1", 0.0, 1.0, 0.93)]
