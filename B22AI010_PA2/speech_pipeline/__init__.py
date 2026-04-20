"""Speech processing pipeline package."""

from .settings import PipelineConfig
from .apps.evaluation_app import compose_report
from .apps.pipeline_app import execute_pipeline

__all__ = ["PipelineConfig", "execute_pipeline", "compose_report"]

