from datetime import datetime

from src.config.loader import ConfigLoader
from src.discovery.discovery_service import DiscoveryService
from src.discovery.provider_factory import ProviderFactory
from src.domain.execution import Execution
from src.domain.execution_context import ExecutionContext
from src.planner.execution_planner import ExecutionPlanner
from src.utils.constants import DEFAULT_CONFIG_FILE
from src.services.inventory_service import InventoryService

class ExecutionService:
    """
    Coordinates the execution lifecycle.
    """

    def execute(self, request):

        # -------------------------------------------------------------
        # Load Configuration
        # -------------------------------------------------------------

        print("\nLoading configuration...")

        config = ConfigLoader().load(DEFAULT_CONFIG_FILE)

        print("✓ Configuration loaded.")

        # -------------------------------------------------------------
        # Create Execution
        # -------------------------------------------------------------

        print("\nCreating execution...")

        execution = Execution(
            change_number=request.change_number,
            mode=request.mode,
            started_at=datetime.now(),
            initiated_by="Arjun",

            environment=request.environment,
    requested_groups=request.requested_groups,
    requested_clusters=request.requested_clusters,

    parallel_workers=request.parallel_workers,
)

        context = ExecutionContext(
            config=config,
            execution=execution,
        )

        print("✓ Execution initialized.")

        # -------------------------------------------------------------
        # Resolve Target Clusters
        # -------------------------------------------------------------

        print("\nResolving target clusters...")

        inventory = InventoryService()

        context.clusters = inventory.get_clusters(
            request.environment,
            request.requested_groups,
        )

        print(f"✓ Selected {len(context.clusters)} target cluster(s).")

        # -------------------------------------------------------------
        # Build Execution Plan
        # -------------------------------------------------------------

        planner = ExecutionPlanner()

        context.plan = planner.create_plan(context)

        # -------------------------------------------------------------
        # Display Execution Plan
        # -------------------------------------------------------------

        print()
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

        for idx, cluster in enumerate(context.plan.clusters, start=1):
            print(
                f"{idx:<4}"
                f"{cluster.name:<30}"
                f"{cluster.platform:<15}"
                f"{cluster.environment:<12}"
                f"{cluster.group:<15}"
                f"{cluster.region}"
            )

        print("\nCollectors")
        print("-" * 70)

        if context.plan.collectors:
            for collector in context.plan.collectors:
                print(f"✓ {collector}")
        else:
            print("No collectors selected.")

        print("\nExecution ready.")

        return context