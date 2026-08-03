class MainMenu:

    @staticmethod
    def show():

        print()

        print("=" * 70)

        print(" AI-assisted Multi-Cluster Kubernetes Change Validation Platform")

        print("=" * 70)

        print()

        print("Main Menu")

        print("---------")

        print()

        print("1. Start PRE Validation")

        print("2. Start POST Validation")

        print("3. Compare PRE vs POST")

        print("4. View Reports")

        print("5. Dashboard")

        print("6. Exit")

        print()

        while True:
            choice = input("Select: ")
            if choice in ["1", "2", "3", "4", "5", "6"]:
                return choice
            print("Invalid selection.")

    @staticmethod
    def show_summary(request, inventory):
        groups = (
            "ALL"
            if not request.requested_groups
            else ", ".join(request.requested_groups)
        )

        cluster_count = len(
            inventory.get_clusters(
                request.environment,
                request.requested_groups,
            )
        )

        print()

        print("=" * 60)
        print("Execution Summary")
        print("=" * 60)

        print(f"Change Number    : {request.change_number}")
        print(f"Mode             : {request.mode}")
        print(f"Environment      : {request.environment}")
        print(f"Groups           : {groups}")
        print(f"Target Clusters  : {cluster_count}")
        print(f"Parallel Workers : {request.parallel_workers}")