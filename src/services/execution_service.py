from datetime import datetime

from src.config.loader import ConfigLoader
from src.discovery.discovery_service import DiscoveryService
from src.discovery.provider_factory import ProviderFactory
from src.domain.execution import Execution
from src.domain.execution_context import ExecutionContext
from src.planner.execution_planner import ExecutionPlanner
from src.utils.constants import DEFAULT_CONFIG_FILE


class ExecutionService:
    """
    Coordinates the overall execution flow.

    Responsibilities:
    - Load application configuration
    - Create execution context
    - Discover target clusters
    - Generate execution plan

    Responsibilities NOT handled here:
    - CLI parsing
    - Collector execution
    - Snapshot generation
    - HTML reporting
    - Dashboard updates
    """

    def run(self):

        # ------------------------------------------------------------------
        # Load Configuration
        # ------------------------------------------------------------------

        print("Loading configuration...")

        config = ConfigLoader().load(DEFAULT_CONFIG_FILE)

        print("✓ Configuration loaded.\n")

        # ------------------------------------------------------------------
        # Create Execution
        # ------------------------------------------------------------------

        print("Creating execution...")

        execution = Execution(
            change_number="CHG-DEMO-001",
            mode=config.execution.mode.upper(),
            started_at=datetime.now(),
            initiated_by="Arjun",
            environment="ALL",
            parallel_workers=15,
)

        context = ExecutionContext(
            config=config,
            execution=execution,
        )

        print("✓ Execution initialized.\n")

        # ------------------------------------------------------------------
        # Discover Clusters
        # ------------------------------------------------------------------

        print("Discovering Kubernetes clusters...")

        provider = ProviderFactory.create()

        print(f"Cluster Provider : {provider.__class__.__name__}")

        discovery = DiscoveryService(provider)

        context.clusters = discovery.discover_clusters()

        print()

        # ------------------------------------------------------------------
        # Build Execution Plan
        # ------------------------------------------------------------------

        planner = ExecutionPlanner()

        context.plan = planner.create_plan(context)

        # ------------------------------------------------------------------
        # Display Execution Plan
        # ------------------------------------------------------------------

        print("=" * 70)
        print("Execution Plan")
        print("=" * 70)

        print(f"{'Change Number':25}: {context.plan.execution.change_number}")
        print(f"{'Execution Mode':25}: {context.plan.execution.mode}")
        print(f"{'Cluster Count':25}: {len(context.plan.clusters)}")
        print(f"{'Worker Threads':25}: {context.plan.worker_count}")
        print(f"{'Snapshot Directory':25}: {context.plan.snapshot_directory}")
        print(f"{'Report Directory':25}: {context.plan.report_directory}")
        print(f"{'Comparison Enabled':25}: {context.plan.comparison_enabled}")
        print(f"{'Dashboard Enabled':25}: {context.plan.dashboard_enabled}")

        print("\nTarget Clusters")
        print("-" * 70)

        print(
    f"{'#':<4}"
    f"{'Cluster':<30}"
    f"{'Platform':<15}"
    f"{'Environment':<12}"
    f"{'Group':<15}"
    f"{'Region'}"
)
        print("-" * 90)

        for idx, item in enumerate(context.plan.clusters, start=1):
            # item is expected to have attributes: name, platform, environment, group, region
            print(
                f"{idx:<4}"
                f"{getattr(item, 'name', ''):<30}"
                f"{getattr(item, 'platform', ''):<15}"
                f"{getattr(item, 'environment', ''):<12}"
                f"{getattr(item, 'group', ''):<15}"
                f"{getattr(item, 'region', '')}"
            )

        print("\nCollectors")
        print("-" * 70)
        print(context.plan.collectors)
        if context.plan.collectors:
            for collector in context.plan.collectors:
                print(f"✓ {collector}")
        else:
            print("No collectors selected.")

        print("\nApplication ready.")

        return context