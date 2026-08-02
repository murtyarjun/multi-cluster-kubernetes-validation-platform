from .models import Config


class ConfigValidator:
    """Validates application configuration."""

    @staticmethod
    def validate(config: Config) -> None:
        if config.execution.max_parallel_clusters <= 0:
            raise ValueError(
                "max_parallel_clusters must be greater than zero."
            )

        if config.execution.timeout_seconds <= 0:
            raise ValueError(
                "timeout_seconds must be greater than zero."
            )

        if config.execution.mode.lower() not in ("pre", "post"):
            raise ValueError(
                "execution.mode must be 'pre' or 'post'."
            )