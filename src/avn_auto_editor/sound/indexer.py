from __future__ import annotations


class SoundIndexer:
    def index(self, library_path: str) -> list[str]:
        return [f"{library_path}/sample.wav"]
