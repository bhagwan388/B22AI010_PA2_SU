"""Refactored entry point for the benchmark evaluation suite."""

from __future__ import annotations

from ..benchmark import cli_main as _evaluation_cli_main
from ..benchmark import compose_report


def main() -> None:
    """CLI entry point for evaluation."""

    _evaluation_cli_main()


build_report = compose_report
