from unittest import TestCase
import student
import validator

class Teststudent(TestCase):
        def setUp(self):
            self.student = student.Student(full_name="Adebayo kehinde", password="123", email="adebayosamuel6667@gmail.com", student_id="1234")

        def test_full_name(self):
            self.assertEqual(self.student.full_name, "Adebayo kehinde")
            self.student.full_name = "Adebayo kehinde"
            self.assertEqual(self.student.full_name, "Adebayo kehinde")

        def test_student_id(self):
            self.assertEqual(self.student.student_id, "1234")
            self.student.student_id = "1234"
            self.assertEqual(self.student.student_id("1234"))

