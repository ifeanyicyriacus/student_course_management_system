import sys

from scms.instructor_menu import InstructorMenu
from scms.student_menu import StudentMenu
from scms.ui_styling import TextColor, ClearingText
from scms.validator import Validator
from scms.student import Student
from scms.instructor import Instructor
from scms.portal import Portal
APP_NAME = "SCMS"

class MainMenu(TextColor, ClearingText):
    portal = Portal()
    current_user: Student | Instructor | None = None

    def start(self) -> None:
        print_line()
        print(success_message(f"""
                                                                *** {APP_NAME} ***
                                            Your No 1 Trusted Student Course Management System
                        """))
        print_line()
        self.main_menu(success_message("Welcome to Student Course Management System.".center(150)))

    def main_menu(self, prompt:str) -> None:
        clear_screen()
        student = "student"
        instructor = "instructor"
        menu_prompt = """
        Kindly choose one of the options:
        1. Register as a new student
        2. Register as a new instructor
        3. Login to your account
        0. Exit the program
        
        """ + prompt + "\n>>>"

        user_input:int = input_int(menu_prompt)
        match user_input:
            case 1: self.register(student)
            case 2: self.register(instructor)
            case 3: self.login()
            case 0: exit_program()
            case _: self.main_menu(error_message("Invalid selection: available options are (1 - 3 & 0) Try again"))
        self.main_menu(menu_prompt)

    def register(self, user_type:str) -> None:
        print("""
                                                    *** Welcome To The Registration Zone ***

                                    We're thrilled to have you join our community! Lets get you started! \U0001F60A
                """)
        print_line()
        full_name = input_str("Full Name: ")
        email = input_email()
        if self.portal.check_duplicate_email(email):
            return self.main_menu(error_message("Registration Failed: Email already registered."))
        password = input_password()
        confirm_password = input_password("Confirm Password: ")
        if password != confirm_password:
            return self.main_menu(error_message("Passwords do not match: Please try again."))
        try:
            if user_type.lower() == "student":
                self.portal.register_student(full_name, email, password)
            elif user_type.lower() == "instructor":
                self.portal.register_instructor(full_name, email, password)
        except ValueError as e:
            return self.main_menu(error_message(f"Registration Unsuccessful: {e}"))
        return self.main_menu(success_message(f"{user_type.title()} Registration Successful: \n"
                                              f"Welcome {full_name.title()}, 🎉 Now you can login!"))

    def login(self) -> None:
        print("Login to your account")
        email = input_email()
        password = input_password()
        self.current_user = self.portal.login(email, password)
        if self.current_user is None:
            return self.main_menu(error_message("Login Failed: Incorrect email or password."))
        elif self.current_user is Student:
            return self.student_dashboard(success_message(f"Student Login Successful! Welcome back, {self.current_user.full_name}!"))
        else:
            return self.instructor_dashboard(success_message(f"Instructor Login Successful! Welcome back, {self.current_user.full_name}!"))

    def student_dashboard(self, prompt:str) -> None:
        clear_screen()
        print_line()
        print("Welcome to Student Dashboard".center(150))
        print_line()

        student_menu:StudentMenu = StudentMenu(self.current_user)
        menu_prompt = """
        Choose one of the options:
        1.Enroll in a course
        2.View my courses
        3.View my grades
        4.View my instructor
        5.Manage your account
        6.Logout
        0.Exit
    
        """ + prompt + "\n>>>"
        choice = input_int(menu_prompt)
        match choice:
            case 1: student_menu.enroll_in_course()
            case 2: student_menu.view_my_courses()
            case 3: student_menu.view_my_grades()
            case 4: student_menu.view_my_instructor()
            case 5: student_menu.manage_account()
            case 6: self.logout()
            case 0: exit_program()
            case _: self.student_dashboard(error_message("Invalid selection: available options are (1 - 6 & 0) Try again"))


    def instructor_dashboard(self, prompt) -> None:
        clear_screen()
        print_line()
        print("Welcome to Instructor Dashboard".center(150))
        print_line()

        instructor_menu:InstructorMenu = InstructorMenu(self.current_user)
        menu_prompt = """
        Choose one of the options:
        1. Create a new course
        2. Assign grades
        3. Edit grades (coming soon)
        4. View students enrolled in a course
        5. Logout
        0. Exit
    
        """ + prompt + "\n>>>"
        choice = input(menu_prompt)
        match choice:
            case 1: instructor_menu.create_new_course()
            case 2: instructor_menu.assign_grades()
            case 3: instructor_menu.edit_grades()
            case 4: instructor_menu.view_students_enrolled_in_course()
            case 5: self.logout()
            case 0: exit_program()
            case _: self.instructor_dashboard(error_message("Invalid selection: available options are (1 - 5 & 0) Try again"))

    def logout(self) -> None:
        self.current_user = None
        return self.main_menu(info_message("Logout Successful: \n"))


def exit_program():
    print("Thank you for using SCMS. Goodbye friend!")
    sys.exit(0)
    
def print_line() -> None:
        print("====================================================================================================================================================")

def input_email() -> str:
    email = input_str("Enter your email: ")
    if Validator.validate_email(email):
        return email
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

def input_int(prompt:str) -> int:
    try:
        number = int(input(prompt).strip())
        return number
    except ValueError:
        print(error_message("Invalid input. Enter an integer and Try again."))
        return input_int(prompt)

def input_password(prompt = "Enter your password: "):
    value = input(prompt).strip()
    if Validator.validate_password(value):
        return value
    else:
        print(error_message("Invalid input. Enter a password and Try again."))
        print(info_message("Must contain 8 - 16 characters [uppercase, lowercase, number and special characters.]"))
        return input_password(prompt)

def error_message(message:str) -> str:
    return "\033[31m" + message + "\033[0m"

def success_message(message:str) -> str:
    return "\033[32m" + message + "\033[0m"

def info_message(message:str) -> str:
    return "\033[33m" + message + "\033[0m"

def clear_screen() -> None:
    print("\033[H\033[2J")

MainMenu().start()








