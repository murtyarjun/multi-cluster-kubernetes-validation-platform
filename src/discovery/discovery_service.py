from src.discovery.provider import ClusterProvider
from src.domain.cluster import Cluster


class DiscoveryService:
    """Coordinates cluster discovery."""

    def __init__(self, provider: ClusterProvider):
        self.provider = provider

    def discover_clusters(self) -> list[Cluster]:
        return self.provider.get_clusters()