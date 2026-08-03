from dataclasses import dataclass


@dataclass
class Cluster:
    """
    Represents a Kubernetes cluster managed by the platform.
    """

    name: str
    context: str

    platform: str = "Unknown"

    environment: str = "Unknown"

    group: str = "Default"

    region: str = "Unknown"

    reachable: bool = False