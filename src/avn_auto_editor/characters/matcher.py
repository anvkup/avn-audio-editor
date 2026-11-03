from __future__ import annotations


class CharacterMatcher:
    def match(self, speaker_names: list[str], profiles: list) -> dict[str, str]:
        mapping: dict[str, str] = {}
        for idx, speaker in enumerate(speaker_names):
            mapping[speaker] = profiles[idx % len(profiles)].name if profiles else speaker
        return mapping
