from pathlib import Path

from src.discovery.demo_provider import DemoProvider
from src.discovery.kubeconfig_provider import KubeconfigProvider
from src.discovery.provider import ClusterProvider


class ProviderFactory:
    """Creates the appropriate cluster provider."""

    @staticmethod
    def create() -> ClusterProvider:

        kubeconfig = Path.home() / ".kube" / "config"

        if kubeconfig.exists():
            return KubeconfigProvider()

        return DemoProvider()