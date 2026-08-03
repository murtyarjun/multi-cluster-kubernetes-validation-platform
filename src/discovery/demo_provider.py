from abc import abstractmethod
from pathlib import Path

import yaml

from src.discovery.provider import ClusterProvider
from src.domain.cluster import Cluster


class DemoProvider(ClusterProvider):
    """Loads demo cluster inventory from YAML."""

    def get_clusters(self) -> list[Cluster]:

        inventory = (
            Path(__file__).resolve().parents[2]
            / "sample-data"
            / "demo-clusters.yaml"
        )

        with inventory.open("r", encoding="utf-8") as stream:
            data = yaml.safe_load(stream)

        return [
            Cluster(
                name=item["name"],
                context=item["context"],
                platform=item["platform"],
                environment=item["environment"],
                group=item["group"],
                region=item["region"],
            )
            for item in data["clusters"]
        ]