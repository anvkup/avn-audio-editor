from __future__ import annotations

from dataclasses import dataclass


@dataclass
class SoundAsset:
    name: str
    category: str
    path: str
    duration_seconds: float = 0.0


class SoundLibrary:
    def __init__(self) -> None:
        self.assets: list[SoundAsset] = []

    def add_asset(self, asset: SoundAsset) -> None:
        self.assets.append(asset)
