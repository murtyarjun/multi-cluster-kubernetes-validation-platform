from pathlib import Path

from src.domain.execution_plan import ExecutionPlan


class ExecutionPlanner:

    def create_plan(self, context):

        execution = context.execution

        snapshot_directory = (
            Path("snapshots")
            / execution.change_number
            / execution.mode.lower()
        )

        report_directory = (
            Path("reports")
            / execution.change_number
        )

        comparison_enabled = (
            execution.mode.upper() == "POST"
        )

        return ExecutionPlan(
            execution=execution,
            clusters=context.clusters,
            collectors=[
                 "Node Collector",
            ],
            snapshot_directory=snapshot_directory,
            report_directory=report_directory,
            comparison_enabled=comparison_enabled,
            dashboard_enabled=True,
            worker_count=execution.parallel_workers,
     )