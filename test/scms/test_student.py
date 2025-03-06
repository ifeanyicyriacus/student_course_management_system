import unittest

from scms.student import Student


class StudentTestCase(unittest.TestCase):
    id = 0
    full_name = "sample name"
    email="sample email"
    password = "password"


    def setUp(self):
        self.student = Student(
            student_id= self.id,
            full_name= self.full_name,
            email= self.email,
            password= self.password
        )

    def