from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from avn_auto_editor.core.models import PipelineResult, ProductionProject


@dataclass
class ProcessingPipeline:
    project: ProductionProject
    stages: List[PipelineResult] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.stages:
            self.stages = [
                PipelineResult("Script analysis", True, "Narrative structure and dialogue beats identified.", 0.93),
                PipelineResult("Transcription", True, "Dialogue transcription aligned to script timestamps.", 0.91),
                PipelineResult("Speaker matching", True, "Character profiles matched to confirmed vocal identities.", 0.88),
                PipelineResult("SFX and ambience", False, "Awaiting sound-design library indexing.", 0.76),
                PipelineResult("Mix and balance", False, "Processing rules pending final review.", 0.79),
                PipelineResult("REAPER export", False, "Project package not yet generated.", 0.72),
            ]

    def advance(self, stage_name: str, complete: bool, message: str, confidence: float) -> None:
        for idx, item in enumerate(self.stages):
            if item.stage == stage_name:
                self.stages[idx] = PipelineResult(stage_name, complete, message, confidence)
                return
        self.stages.append(PipelineResult(stage_name, complete, message, confidence))

    def summary(self) -> dict[str, float]:
        completed = sum(1 for stage in self.stages if stage.complete)
        total = max(len(self.stages), 1)
        return {
            "completion": round((completed / total) * 100, 1),
            "average_confidence": round(sum(stage.confidence for stage in self.stages) / total, 2),
        }

    def queue_items(self) -> List[str]:
        return [
            "Cross-check VO gaps in Chapter 3",
            "Review room tone replacement near Intro scene",
            "Confirm music cue alignment for Act II",
        ]
