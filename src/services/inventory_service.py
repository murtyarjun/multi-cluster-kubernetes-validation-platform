from src.discovery.discovery_service import DiscoveryService
from src.discovery.provider_factory import ProviderFactory


class InventoryService:
    """
    Provides inventory information to the UI.
    """

    def __init__(self):

        provider = ProviderFactory.create()

        self.discovery = DiscoveryService(provider)

        self.clusters = self.discovery.discover_clusters()

    def get_environments(self) -> list[str]:
        """Returns all available environments."""

        return sorted(
            {cluster.environment for cluster in self.clusters}
        )

    def get_group_summary(self, environment: str) -> list[tuple[str, int]]:
        """Returns available groups and cluster count."""

        summary = {}

        for cluster in self.clusters:

            if environment != "ALL" and cluster.environment != environment:
                continue

            summary.setdefault(cluster.group, 0)
            summary[cluster.group] += 1

        return sorted(summary.items())

    def get_groups(self, environment: str) -> list[str]:
        """Returns group names only."""

        return [group for group, _ in self.get_group_summary(environment)]

    def get_clusters(self, environment: str, groups: list[str]):
        """Returns matching clusters."""

        return [
            cluster
            for cluster in self.clusters
            if (
                (environment == "ALL"
                 or cluster.environment == environment)
                and (
                    not groups
                    or cluster.group in groups
                )
            )
        ]