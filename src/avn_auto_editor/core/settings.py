from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class AppSettings:
    dark_theme: bool = True
    auto_transcription: bool = True
    speaker_matching: bool = True
    sound_recommendations: bool = True
    music_recommendations: bool = True
    auto_mix: bool = True
    generate_reaper_project: bool = True
    review_threshold: float = 0.82
    output_directory: str = "~/AVN Projects"
    preferred_sample_rate: int = 48000
    preferred_bit_depth: int = 24
    reaper_path: str = "/Applications/REAPER.app"
    notes: str = "Production defaults for completed dialogue and scripted audio projects."
    recent_projects: list[str] = field(default_factory=lambda: ["Lumen House", "The Last Broadcast", "Night Shift"])

    @classmethod
    def defaults(cls) -> "AppSettings":
        return cls()
