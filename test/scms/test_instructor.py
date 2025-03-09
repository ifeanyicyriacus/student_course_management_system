from unittest import TestCase
from src.scms.instructor import Instructor

class TestInstructor(TestCase):
    instructor_id = "1234"
    full_name = "Onyinyechi Ekezie"
    password = "123"
    email = "onyii@semicolon.com"
    empty = ""

    def setUp(self):
        self.instructor = Instructor(self.instructor_id, self.full_name, self.email, self.password)

    def test_instructor_id(self):
        self.assertEqual(self.instructor.instructor_id, self.instructor_id)
        self.instructor.instructor_id = "NEW_ID"
        self.assertEqual(self.instructor.instructor_id, "NEW_ID")

    def test_setting_invalid_instructor_id_value_raises_error(self):
        with self.assertRaises(ValueError):
            Instructor(self.empty, self.full_name, self.email, self.password)
        with self.assertRaises(ValueError):
            self.instructor.instructor_id = ""
        with self.assertRaises(ValueError):
            self.instructor.instructor_id = "         "