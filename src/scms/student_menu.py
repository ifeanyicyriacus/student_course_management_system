from src.scms.course import Course
from src.scms.portal import Portal
from src.scms.student import Student
from src.std_utility.ui_styling import StringFormatting
from src.std_utility.io_function import Validator, input_str, clear_screen, error_message, input_int, exit_program, print_line


def start(self):
    print_line()
    self.student_menu(f"Student Login Successful! Welcome back, {self._student.full_name}!", )

def student_menu(self, prompt: str) -> None:
    clear_screen()
    print_line()
    print("Welcome to Student Dashboard".center(150, "-"))
    print_line()

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
        case 1: self.enroll_in_course()
        case 2: self.view_my_courses()
        case 3: self.view_my_grades()
        case 4: self.view_my_instructor()
        case 5: self.manage_account()
        case 6: pass
        case 0: exit_program()
        case _:
            self.student_menu(error_message("Invalid selection: available options are (1 - 6 & 0) Try again"))

def display_courses(courses:[Course]) -> str:
    text = StringFormatting("Courses:\n").underline().bold().green()
    text += StringFormatting(f'{"ID":>10} - {"NAME":>20}\n').bold()
    for course in courses:
        text += f"{course.course_id} - {course.course_name}\n"
    return text

class StudentMenu:
    def __init__(self, student:Student, portal:Portal):
        self._student:Student = student
        self._portal:Portal = portal

    def enroll_in_course(self):
        # fetch all course
        # courses = self.portal.get_all_courses
        # display_courses(courses)//course id and name
        # course_id:str = input_str(f"{display_courses}\nEnter a course ID from above: \n>>> ")
        # if Validator.validate_course_id_format(course_id):
        #     for course in self._portal.courses:
        #         if course.course_id.lower() == course_id.lower():
        #             self._portal.add_enrollment(course_id, student_id)
        #
        #
        #
        # course_id, Course_name
        #            Course_description
        # eg. 1. Maths
        # eg. 2. English
        # switch choice
        # case 1: enroll(cos000001, stu000002)
        #
        pass

    def view_my_courses(self):
        # fetch all courses
        # for there student_id == self._portal
    #     my_courses = self.portal.get_course_by(student_id)
        # display_courses(my_courses)//course id and name
        pass

    def view_my_grades(self):
        # my_enrollments = self.portal.get_enrollment_by_student_id()
        # display_enrollments(my_enrollments) //course_id | course_id

        # after displaying "show, a simple press enter to continue"
        # input_escape("press enter to continue") used as a pause anything goes
        pass

    def view_my_instructor(self):
        #  course | instructors
        #
        pass

    def manage_account(self):

        pass


