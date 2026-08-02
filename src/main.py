from src.config.loader import ConfigLoader
from src.utils.constants import DEFAULT_CONFIG_FILE
from src.utils.logger import configure_logger


def print_banner(config):
    print("=" * 70)
    print(f" {config.application.name}")
    print("=" * 70)
    print()

    print(f"Version            : {config.application.version}")
    print(f"Execution Mode     : {config.execution.mode.upper()}")
    print(
        f"Parallel Clusters  : {config.execution.max_parallel_clusters}"
    )
    print(f"Kubeconfig         : {config.kubernetes.kubeconfig}")
    print()

    print("✓ Configuration loaded successfully.")


def main():

    loader = ConfigLoader()

    config = loader.load(DEFAULT_CONFIG_FILE)

    configure_logger(config.logging.level)

    print_banner(config)


if __name__ == "__main__":
    main()