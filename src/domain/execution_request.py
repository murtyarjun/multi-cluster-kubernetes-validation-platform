from dataclasses import dataclass, field


@dataclass
class ExecutionRequest:
    """
    Represents the user's execution request collected
    from the interactive console.
    """

    # Required
    change_number: str
    mode: str

    # Optional filters
    environment: str = "ALL"

    requested_groups: list[str] = field(default_factory=list)

    requested_clusters: list[str] = field(default_factory=list)

    # Execution settings
    parallel_workers: int = 15