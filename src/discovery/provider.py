from abc import ABC, abstractmethod

from src.domain.cluster import Cluster


class ClusterProvider(ABC):
    """Abstract provider for discovering Kubernetes clusters."""

    @abstractmethod
    def get_clusters(self) -> list[Cluster]:
        """Return discovered clusters."""
        raise NotImplementedError