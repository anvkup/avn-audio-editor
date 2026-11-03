from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ScriptLine:
    index: int
    character: str
    text: str


class ScriptParser:
    def parse(self, script_path: str) -> list[ScriptLine]:
        return [ScriptLine(1, "Narrator", "Welcome to the story.")]
