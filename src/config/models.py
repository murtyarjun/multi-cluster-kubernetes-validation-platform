from dataclasses import dataclass


@dataclass(frozen=True)
class ApplicationConfig:
    """Application metadata."""

    name: str
    version: str


@dataclass(frozen=True)
class ExecutionConfig:
    """Execution settings."""

    mode: str
    max_parallel_clusters: int
    timeout_seconds: int


@dataclass(frozen=True)
class KubernetesConfig:
    """Kubernetes connectivity configuration."""

    kubeconfig: str


@dataclass(frozen=True)
class OutputConfig:
    """Output directory configuration."""

    reports_dir: str
    json_dir: str
    html_dir: str


@dataclass(frozen=True)
class LoggingConfig:
    """Logging configuration."""

    level: str


@dataclass(frozen=True)
class Config:
    """Root application configuration."""

    application: ApplicationConfig
    execution: ExecutionConfig
    kubernetes: KubernetesConfig
    output: OutputConfig
    logging: LoggingConfig