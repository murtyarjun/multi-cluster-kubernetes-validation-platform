from dataclasses import dataclass, field
from datetime import datetime

from .cluster import Cluster


@dataclass
class Execution:
    """
    Represents a maintenance validation request
    entered by the engineer.
    """

    change_number: str
    mode: str
    started_at: datetime
    initiated_by: str

    environment: str = "ALL"

    requested_groups: list[str] = field(default_factory=list)

    requested_clusters: list[str] = field(default_factory=list)

    parallel_workers: int = 15

    clusters: list[Cluster] = field(default_factory=list)