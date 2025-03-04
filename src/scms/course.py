from scms.enrollment import Enrollment
from scms.instructor import Instructor
from scms.student import Student


class Course:
    def __init__(self, course_id:str, course_name:str, course_description:str, instructor_assigned:Instructor):
        self.course_id = course_id
        self.course_name = course_name
        self.course_description = course_description
        self.instructor_assigned = instructor_assigned
        self.enrollments:[Enrollment] = []


        def add_student(self, student:Student):
            pass

        def remove_student(self, student:Student):
            pass