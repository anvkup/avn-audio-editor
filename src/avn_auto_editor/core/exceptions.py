from __future__ import annotations


class AVNError(Exception):
    """Base exception for AVN project operations."""


class ProjectLoadError(AVNError):
    """Raised when a project cannot be loaded from disk."""


class AudioProcessingError(AVNError):
    """Raised when audio processing fails."""


class ExportError(AVNError):
    """Raised when a REAPER export fails."""
