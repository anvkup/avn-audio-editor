from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TranscriptSegment:
    start: float
    end: float
    speaker: str
    text: str


class TranscriptionEngine:
    def __init__(self, model_name: str = "local-whisper") -> None:
        self.model_name = model_name

    def transcribe(self, audio_path: str) -> list[TranscriptSegment]:
        return [TranscriptSegment(0.0, 1.0, "Unknown", "Placeholder transcript segment.")]
