from src.ui.validator import InputValidator


class Prompts:

    @staticmethod
    def ask_change_number():

        print()
        print("Enter Change Number")
        print("-------------------")

        while True:

            value = input("> ")

            try:
                return InputValidator.validate_change_number(value)

            except ValueError as ex:
                print(f"❌ {ex}")

    @staticmethod
    def ask_environment(service):

        environments = service.get_environments()

        print()
        print("Available Environments")
        print("----------------------")

        for index, env in enumerate(environments, start=1):
            print(f"{index}. {env}")

        print(f"{len(environments) + 1}. ALL")

        while True:

            choice = input("> ").strip()

            if choice.isdigit():

                choice = int(choice)

                if 1 <= choice <= len(environments):
                    return environments[choice - 1]

                if choice == len(environments) + 1:
                    return "ALL"

            print("Invalid selection.")

    @staticmethod
    def ask_groups(service, environment):

        groups = service.get_group_summary(environment)

        print()
        print("Available Groups")
        print("----------------")

        for index, (group, count) in enumerate(groups, start=1):
            suffix = "cluster" if count == 1 else "clusters"
            print(f"{index}. {group:<18} ({count} {suffix})")

        print(f"{len(groups) + 1}. ALL")

    @staticmethod
    def confirm_execution() -> bool:

     print()
     print("-" * 60)

     while True:

        answer = input("Proceed with execution? (Y/N): ").strip().upper()

        if answer == "Y":
            return True

        if answer == "N":
            return False

        print("Please enter Y or N.")

        while True:

            choice = input("> ").strip()

            if choice.isdigit():

                choice = int(choice)

                if 1 <= choice <= len(groups):
                    return [groups[choice - 1][0]]

                if choice == len(groups) + 1:
                    return []

            print("Invalid selection.")