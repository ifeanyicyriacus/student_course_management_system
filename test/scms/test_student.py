import unittest

from scms.course import Course
from scms.instructor import Instructor
from scms.student import Student

class StudentTestCase(unittest.TestCase):
    student_id = "0"
    instructor_id = "1"
    full_name = "sample name"
    email = "sample email"
    password = "password"

    course_id = "12"
    course_name = "sample course"
    course_description = "sample description"
    instructor_assigned = Instructor(instructor_id, full_name, email, password)


    def setUp(self):
        self.student = Student(self.id, self.full_name, self.email, self.password)
        self.course = Course(self.course_id, self)
    def test_student_can_enroll_course(self):
        self.student.enroll()
        # self.assertListEqual([], self.student.enrolled_courses)