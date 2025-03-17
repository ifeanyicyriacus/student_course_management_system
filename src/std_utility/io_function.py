import sys
from src.scms.validator import Validator

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

def input_course_id() -> str:
    value = input("Enter course ID: ")
    if Validator.validate_course_id(value):
        return value
    else:
        print(error_message("Invalid input. Enter a valid course ID."))
        print(info_message("Course ID must be in the format COU####."))
        return input_course_id()

def input_student_id() -> str:
    value = input("Enter student ID: ")
    if Validator.validate_student_id(value):
        return value
    else:
        print(error_message("Invalid input. Enter a valid student ID."))
        print(info_message("Student ID must be in the format STU######."))
        return input_student_id()

def input_instructor_id() -> str:
    value = input("Enter instructor ID: ")
    if Validator.validate_instructor_id(value):
        return value
    else:
        print(error_message("Invalid input. Enter a valid instructor ID."))
        print(info_message("Instructor ID must be in the format INS######."))
        return input_instructor_id()

def score_to_grade(score:int) -> str:
    if score < 0 or score > 100:
        return error_message(f"Score must be between 0 and 100.")
    if score > 70: return "A"
    elif score > 60: return "B"
    elif score > 50: return "C"
    elif score > 40: return "D"
    elif score > 30: return "E"
    else: return "F"

def error_message(message: str) -> str:
    return "\033[31m" + message + "\033[0m"

def success_message(message: str) -> str:
    return "\033[32m" + message + "\033[0m"

def info_message(message: str) -> str:
    return "\033[33m" + message + "\033[0m"

def clear_screen() -> None:
    print("\033[H\033[2J")
