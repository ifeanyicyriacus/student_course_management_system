from src.scms.instructor_menu import InstructorMenu
from src.scms.student_menu import StudentMenu
from src.scms.student import Student
from src.scms.instructor import Instructor
from src.scms.portal import Portal
from src.std_utility.io_function import *

APP_NAME = "SCMS"

class MainMenu:
    _portal = Portal()
    _current_user: Student | Instructor | None = None

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
        if self._portal.check_duplicate_email(email):
            return self.main_menu(error_message("Registration Failed: Email already registered."))
        password = input_password()
        confirm_password = input_password("Confirm Password: ")
        if password != confirm_password:
            return self.main_menu(error_message("Passwords do not match: Please try again."))
        try:
            if user_type.lower() == "student":
                self._portal.register_student(full_name, email, password)
            elif user_type.lower() == "instructor":
                self._portal.register_instructor(full_name, email, password)
        except ValueError as e:
            return self.main_menu(error_message(f"Registration Unsuccessful: {e}"))
        return self.main_menu(success_message(f"{user_type.title()} Registration Successful: \n"
                                              f"Welcome {full_name.title()}, 🎉 Now you can login!"))

    def login(self) -> None:
        print("Login to your account")
        email = input_email()
        password = input_password()

        self._current_user = self._portal.login(email, password)

        if self._current_user is None:
            return self.main_menu(error_message("Login Failed: Incorrect email or password."))
        elif type(self._current_user) is Student:
            StudentMenu(self._current_user, self._portal).start()
        else:
            InstructorMenu(self._current_user, self._portal).start()
        self.logout()

    def logout(self) -> None:
        self._current_user = None
        return self.main_menu(info_message("Logout Successful: \n"))


MainMenu().start()








