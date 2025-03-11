from src.scms.course import Course
from scms.portal import Portal
from scms.student import Student
from std_utility.ui_styling import StringFormatting
from std_utility.io_function import Validator, input_str

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
        # display_courses(self._portal.courses)
        # course_id:str = input_str(f"{display_courses}\nEnter a course ID from above: \n>>> ")
        # if Validator.valid_course_id_format(course_id):
        #     for course in self._portal.courses:
        #         if course.course_id.lower() == course_id.lower():
        #
        #
        #
        #     self._portal.enrollments.
        # eg. 1. Maths
        # eg. 2. English
        # switch choice
        # case 1: enroll(cos000001, stu000002)
        #
        pass

    def view_my_courses(self):
        pass

    def view_my_grades(self):
        pass

    def view_my_instructor(self):
        pass

    def manage_account(self):
        pass

