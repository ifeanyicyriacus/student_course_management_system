import sys
from scms.validator import Validator

def exit_program():
    print("Thank you for using SCMS. Goodbye friend!")
    sys.exit(0)

def print_line() -> None:
    print(
        "====================================================================================================================================================")

def input_email() -> str:
    email = input_str("Enter your email: ")
    if Validator.validate_email(email):
        return email.lower()
    else:
        print("Invalid email. Try again.")
        return input_email()

def input_str(prompt) -> str:
    value = input(prompt).strip()
    if Validator.validate_input(value):
        return value
    else:
        print(error_message("Invalid input. Try again."))
        return input_str(prompt)

def input_int(prompt: str) -> int:
    try:
        number = int(input(prompt).strip())
        return number
    except ValueError:
        print(error_message("Invalid input. Enter an integer and Try again."))
        return input_int(prompt)

def input_password(prompt="Enter your password: "):
    value = input(prompt).strip()
    if Validator.validate_password(value):
        return value
    else:
        print(error_message("Invalid input. Enter a password and Try again."))
        print(info_message("Must contain 8 - 16 characters [uppercase, lowercase, number and special characters.]"))
        return input_password(prompt)

def error_message(message: str) -> str:
    return "\033[31m" + message + "\033[0m"

def success_message(message: str) -> str:
    return "\033[32m" + message + "\033[0m"

def info_message(message: str) -> str:
    return "\033[33m" + message + "\033[0m"

def clear_screen() -> None:
    print("\033[H\033[2J")
