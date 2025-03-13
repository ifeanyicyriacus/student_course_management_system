from scms.manage_account_menu import ManageAccountMenu
from src.scms.instructor import Instructor
from src.scms.portal import Portal
from std_utility.io_function import input_int, error_message, clear_screen, print_line, exit_program


class InstructorMenu:
    def __init__(self, instructor:Instructor, portal:Portal):
        self._instructor = instructor
        self._portal = portal

    def start(self):
        self.instructor_menu(f"Student Login Successful! Welcome back, {self._instructor.full_name}!")

    def instructor_menu(self, prompt:str) -> None:
        clear_screen()
        print_line()
        print("Welcome to Instructor Dashboard".center(150, "-"))
        print_line()

        menu_prompt = """
        Choose one of the options:
        1. Create a new course
        2. Assign grades
        3. View students enrolled in a course
        4. Manage your account
        5. Logout
        0. Exit

        """ + prompt + "\n>>>"
        choice = input_int(menu_prompt)
        match choice:
            case 1: self.create_new_course()
            case 2: self.assign_grades()
            case 3: self.view_students_enrolled_in_course()
            case 4: ManageAccountMenu(self._instructor, self._portal).start()
            case 5: pass
            case 0: exit_program()
            case _:
                self.instructor_menu(error_message("Invalid selection: available options are (1 - 5 & 0) Try again"))

    def create_new_course(self):
        # prompt collect course name
        # prompt collect course description
        # prompt collect instructor_id
        # if Validator.validate_instructor_id_format(instructor_id):
        #     try:
                # call portal.add_course(name, description, instructor_id)
            # expect
        pass

    def assign_grades(self):

        pass


    def view_students_enrolled_in_course(self):

        pass

    def manage_account(self):

        pass

