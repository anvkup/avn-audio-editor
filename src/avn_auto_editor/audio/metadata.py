from __future__ import annotations

from dataclasses import dataclass


@dataclass
class AudioMetadata:
    duration_seconds: float = 0.0
    sample_rate: int = 48000
    channels: int = 2
    bit_depth: int = 24
    file_size_bytes: int = 0
    format_name: str = "wav"

    @classmethod
    def from_file(cls, path: str) -> "AudioMetadata":
        return cls(file_size_bytes=0, format_name=path.rsplit(".", 1)[-1] if "." in path else "wav")
