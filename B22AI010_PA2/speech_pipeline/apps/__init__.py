"""User-facing application entry points for the speech pipeline."""

from .evaluation_app import compose_report, main as evaluation_main
from .pipeline_app import execute_pipeline, main as pipeline_main

__all__ = ["execute_pipeline", "compose_report", "pipeline_main", "evaluation_main"]