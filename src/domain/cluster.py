from dataclasses import dataclass


@dataclass
class Cluster:
    """Represents a Kubernetes cluster."""

    name: str
    context: str

    reachable: bool = False

    cloud: str = "Unknown"
    environment: str = "Unknown"