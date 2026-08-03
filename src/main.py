from src.services.execution_service import ExecutionService
from src.ui.console import ConsoleUI


def main():

    request = ConsoleUI.start()

    if request is None:
        return

    service = ExecutionService()

    service.execute(request)


if __name__ == "__main__":
    main()