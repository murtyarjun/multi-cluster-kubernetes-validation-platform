from src.services.execution_service import ExecutionService


def main():
    service = ExecutionService()
    service.run()


if __name__ == "__main__":
    main()