"""Refactored entry point for the end-to-end pipeline."""

from __future__ import annotations

from ..runtime import cli_main as _pipeline_cli_main
from ..runtime import execute_pipeline


def main() -> None:
    """CLI entry point for the pipeline application."""

    _pipeline_cli_main()


run_pipeline = execute_pipeline
