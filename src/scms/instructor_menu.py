from src.scms.course import Course
from src.scms.manage_account_menu import ManageAccountMenu
from src.scms.instructor import Instructor
from src.scms.portal import Portal
from std_utility.io_function import input_int, error_message, clear_screen, print_line, exit_program, input_str, \
    success_message


class InstructorMenu:
    def __init__(self, instructor:Instructor, portal:Portal):
        self._instructor = instructor
        self._portal = portal

    def start(self):
        self.instructor_menu(f"Instructor Login Successful! Welcome back, {self._instructor.full_name}!")

    def instructor_menu(self, prompt:str) -> None:
        clear_screen()
        print_line()
        print("Welcome to Instructor Dashboard".center(150, "-"))
        print_line()

        menu_prompt = """
        Choose one of the options:
        1. Create a new course
        2. Assign grades
        3. View students enrolled in my course
        4. Manage your account
        5. Logout
        0. Exit

        """ + prompt + "\n>>>"
        choice = input_int(menu_prompt)
        match choice:
            case 1: self.create_new_course()
            case 2: self.assign_grades()
            case 3: self.view_students_enrolled_in_my_course()
            case 4: ManageAccountMenu(self._instructor, self._portal).start()
            case 5: pass
            case 0: exit_program()
            case _:
                self.instructor_menu(error_message("Invalid selection: available options are (1 - 5 & 0) Try again"))

    def create_new_course(self):
        course_name:str = input_str("Enter course name: ")
        course_description:str = input_str("Enter course description: ")
        instructor_id:str = self._instructor.instructor_id
        try:
            self._portal.add_course(course_name, course_description, instructor_id)
            self.instructor_menu(success_message(f"You have successfully created {course_name}!"))
        except ValueError as e:
            print(error_message("Course not added. Please try again."))
            self.create_new_course()

    def assign_grades(self):
        my_courses:[Course] = self._portal.get_instructors_course_by(self._instructor.instructor_id)
        # first display the instructor his courses if you have any on a list use format
        # My course
        # course_id | course name | no of student enrolled
        # ...  ...    ... .......     ........ ...... .....

        # enter course_id to grade
        #     this will lead to list of student enrolled in this format:
        #       see view_my_grade in student menu
        #       select a student_id to grade
    #           clear-screen
    #           display updated version of course scoresheet
    # while showing enter (0 to go back)



    def view_students_enrolled_in_my_course(self):
        # ask instructor for


        pass

    def manage_account(self):
        ManageAccountMenu(self._instructor, self._portal).start()
        self.instructor_menu("Welcome back to your menu!")

