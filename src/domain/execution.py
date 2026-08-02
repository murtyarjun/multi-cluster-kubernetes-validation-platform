from dataclasses import dataclass, field
from datetime import datetime

from .cluster import Cluster


@dataclass
class Execution:
    """Represents one maintenance validation execution."""

    change_number: str
    mode: str
    started_at: datetime
    initiated_by: str
    clusters: list[Cluster] = field(default_factory=list)