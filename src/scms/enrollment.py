from datetime import datetime

from scms.course import Course
from scms.grade import Grade
from scms.student import Student


class Enrollment:

    def __init__(self, student: Student, course: Course):
        self.enrollment_date = datetime.date.today()
        self.student = student
        self.course = course
        self.grade:Grade = Grade(0, student, course)

    def view_grade(self):
        pass

