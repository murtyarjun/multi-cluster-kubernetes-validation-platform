from pathlib import Path

import yaml

from .models import (
    ApplicationConfig,
    Config,
    ExecutionConfig,
    KubernetesConfig,
    LoggingConfig,
    OutputConfig,
)
from .validator import ConfigValidator


class ConfigLoader:
    """Loads application configuration."""

    def load(self, config_path: str) -> Config:

        path = Path(config_path)

        if not path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {config_path}"
            )

        with path.open("r", encoding="utf-8") as stream:
            data = yaml.safe_load(stream)

        config = Config(
            application=ApplicationConfig(**data["application"]),
            execution=ExecutionConfig(**data["execution"]),
            kubernetes=KubernetesConfig(**data["kubernetes"]),
            output=OutputConfig(**data["output"]),
            logging=LoggingConfig(**data["logging"]),
        )

        ConfigValidator.validate(config)

        return config