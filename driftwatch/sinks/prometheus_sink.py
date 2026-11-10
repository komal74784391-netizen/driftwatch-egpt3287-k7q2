"""Prometheus sink for drift scores."""


def emit(score: float, label: str) -> None:
    print(f"driftwatch_score{{stream={label}}} {score}")
