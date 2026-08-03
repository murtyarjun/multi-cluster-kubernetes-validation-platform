from src.domain.execution_request import ExecutionRequest
from src.ui.menus import MainMenu
from src.ui.prompts import Prompts
from src.services.inventory_service import InventoryService


class ConsoleUI:

    @staticmethod
    def start():

        choice = MainMenu.show()

        if choice == "1":
            return ConsoleUI.start_validation("PRE")

        elif choice == "2":
            return ConsoleUI.start_validation("POST")

        elif choice == "3":
            print("\nCompare feature coming soon.")
            return None

        elif choice == "4":
            print("\nReports feature coming soon.")
            return None

        elif choice == "5":
            print("\nDashboard feature coming soon.")
            return None

        elif choice == "6":
            print("\nGoodbye!")
            return None

    @staticmethod
    def start_validation(mode: str):

        print()

        print(f"Starting {mode} Validation")

        print("-" * 40)

        inventory = InventoryService()

        environment = Prompts.ask_environment(inventory)

        groups = Prompts.ask_groups(
            inventory,
            environment,
        )

        request = ExecutionRequest(
            change_number=Prompts.ask_change_number(),
            mode=mode,
            environment=environment,
            requested_groups=groups,
        )

        return request