from unittest import TestCase
from src.scms.student import Student

class TestStudent(TestCase):
    student_id = "1234"
    full_name = "Adebayo kehinde"
    password = "123"
    email = "adebayosamuel6667@gmail.com"
    empty = ""

    def setUp(self):
        self.student = Student(self.student_id, self.full_name, self.email, self.password)

    def test_student_id(self):
        self.assertEqual(self.student.student_id, self.student_id)
        self.student.student_id = "NEW_ID"
        self.assertEqual(self.student.student_id, "NEW_ID")

    def test_setting_invalid_student_id_value_raises_error(self):
        with self.assertRaises(ValueError):
            Student(self.empty, self.full_name, self.email, self.password)
        with self.assertRaises(ValueError):
            self.student.student_id = ""
        with self.assertRaises(ValueError):
            self.student.student_id = "         "