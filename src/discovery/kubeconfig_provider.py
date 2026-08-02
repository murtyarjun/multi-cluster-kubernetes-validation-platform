from kubernetes import config

from src.discovery.provider import ClusterProvider
from src.domain.cluster import Cluster


class KubeconfigProvider(ClusterProvider):
    """Reads Kubernetes contexts from kubeconfig."""

    def get_clusters(self) -> list[Cluster]:

        contexts, active_context = config.list_kube_config_contexts()

        clusters = []

        for ctx in contexts:
            context_name = ctx["name"]

            clusters.append(
                Cluster(
                    name=context_name,
                    context=context_name,
                    reachable=False,
                )
            )

        return clusters