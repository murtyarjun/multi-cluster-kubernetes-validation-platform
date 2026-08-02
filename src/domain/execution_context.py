from dataclasses import dataclass, field

from src.config.models import Config
from src.domain.cluster import Cluster
from src.domain.execution import Execution


@dataclass
class ExecutionContext:
    """Runtime context shared across the entire execution."""

    config: Config
    execution: Execution
    clusters: list[Cluster] = field(default_factory=list)