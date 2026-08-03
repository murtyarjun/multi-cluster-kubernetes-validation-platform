class InputValidator:

    @staticmethod
    def validate_change_number(change_number: str):

        if not change_number.strip():
            raise ValueError("Change number cannot be empty.")

        return change_number.strip().upper()