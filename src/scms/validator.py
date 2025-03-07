import re

class Validator:
    def __init__(self):
        self.email_pattern = re.compile(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        )

    def validate_email(self, email: str) -> bool:
        return bool(self.email_pattern.match(email))

    def validate_input(self, input_str: str) -> bool:
        return bool(input_str) and input_str.strip() != ""
