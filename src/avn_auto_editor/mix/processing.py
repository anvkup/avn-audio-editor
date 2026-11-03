from __future__ import annotations


class MixProcessor:
    def build_master_chain(self) -> dict[str, float]:
        return {"limiter": -1.0, "loudness": -16.0}
