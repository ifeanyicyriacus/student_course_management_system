import re

class Validator:
    @staticmethod
    def validate_email(email: str) -> bool:
        email_pattern = re.compile(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        )
        return bool(email_pattern.match(email))

    @staticmethod
    def validate_input(input_str: str) -> bool:
        return bool(input_str) and input_str.strip() != ""

    @staticmethod
    def validate_grade(grade:str|int) -> bool:
        if str(grade).isdigit():
            grade = int(grade)
            if 0 <= grade <= 100:
                return True
        else: return False

    @classmethod
    def validate_password(cls, value):
        # Must contain 8 - 16 characters
        # [uppercase, lowercase, number and special characters.]
        return cls.validate_input(value)
