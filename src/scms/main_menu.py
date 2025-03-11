from scms.instructor_menu import InstructorMenu
from scms.student_menu import StudentMenu
from scms.student import Student
from scms.instructor import Instructor
from scms.portal import Portal
from std_utility.io_function import *

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

        print(type(self._current_user))
        if self._current_user is None:
            return self.main_menu(error_message("Login Failed: Incorrect email or password."))
        elif type(self._current_user) is Student:
            return self.student_dashboard(success_message(f"Student Login Successful! Welcome back, {self._current_user.full_name}!"))
        else:
            return self.instructor_dashboard(success_message(f"Instructor Login Successful! Welcome back, {self._current_user.full_name}!"))

    def student_dashboard(self, prompt:str) -> None:
        clear_screen()
        print_line()
        print("Welcome to Student Dashboard".center(150))
        print_line()

        student_menu:StudentMenu = StudentMenu(self._current_user, self._portal)
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
        self.student_dashboard(prompt)

    def instructor_dashboard(self, prompt) -> None:
        clear_screen()
        print_line()
        print("Welcome to Instructor Dashboard".center(150))
        print_line()

        instructor_menu:InstructorMenu = InstructorMenu(self._current_user, self._portal)
        menu_prompt = """
        Choose one of the options:
        1. Create a new course
        2. Assign grades
        3. View students enrolled in a course
        4. Logout
        0. Exit
    
        """ + prompt + "\n>>>"
        choice = input_int(menu_prompt)
        match choice:
            case 1: instructor_menu.create_new_course()
            case 2: instructor_menu.assign_grades()
            case 3: instructor_menu.view_students_enrolled_in_course()
            case 4: self.logout()
            case 0: exit_program()
            case _: self.instructor_dashboard(error_message("Invalid selection: available options are (1 - 4 & 0) Try again"))

    def logout(self) -> None:
        self._current_user = None
        return self.main_menu(info_message("Logout Successful: \n"))


MainMenu().start()








