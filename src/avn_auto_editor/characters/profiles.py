from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CharacterProfile:
    name: str
    voice: str
    role: str = "supporting"
    color_hex: str = "#27C7A5"

    @classmethod
    def from_name(cls, name: str) -> "CharacterProfile":
        return cls(name=name, voice="neutral")
