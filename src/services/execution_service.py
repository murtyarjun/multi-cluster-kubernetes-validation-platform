from datetime import datetime

from src.config.loader import ConfigLoader
from src.discovery.discovery_service import DiscoveryService
from src.discovery.kubeconfig_provider import KubeconfigProvider
from src.discovery.provider_factory import ProviderFactory
from src.domain.execution import Execution
from src.domain.execution_context import ExecutionContext
from src.utils.constants import DEFAULT_CONFIG_FILE
from src.discovery.provider_factory import ProviderFactory


class ExecutionService:

    def run(self):

        print("Loading configuration...")

        config = ConfigLoader().load(DEFAULT_CONFIG_FILE)

        print("✓ Configuration loaded.\n")

        execution = Execution(
            change_number="CHG-DEMO-001",
            mode=config.execution.mode.upper(),
            started_at=datetime.now(),
            initiated_by="Arjun",
        )

        context = ExecutionContext(
            config=config,
            execution=execution,
        )

        print("Creating execution...")
        print("✓ Execution initialized.\n")

        print("Reading kubeconfig...")

        provider = ProviderFactory.create()

        print(f"Cluster Provider : {provider.__class__.__name__}\n")

        discovery = DiscoveryService(provider)

        context.clusters = discovery.discover_clusters()

        print(f"✓ Loaded {len(context.clusters)} context(s).\n")

        for cluster in context.clusters:
            print(
                f"✓ {cluster.name:25}"
                f"{cluster.cloud:12}"
                f"{cluster.environment}"

            )

        print("\nApplication ready.")

        return context