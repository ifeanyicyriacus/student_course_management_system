from unittest import TestCase
from src.scms.enrollment import Enrollment

class TestEnrollment(TestCase):

    def setUp(self):
        self.enrollment1 = Enrollment("courseID1", "studentID1")
        self.enrollment2 = Enrollment("courseID2", "studentID2", "32", "2025-03-09")

    def test_course_id(self):
        self.assertEqual(self.enrollment1.course_id, "courseID1")
        self.assertEqual(self.enrollment2.course_id, "courseID2")

    def test_student_id(self):
        self.assertEqual(self.enrollment1.student_id, "studentID1")
        self.assertEqual(self.enrollment2.student_id, "studentID2")

    def test_grade(self):
        self.assertEqual(self.enrollment1.grade, 0)
        self.assertEqual(self.enrollment2.grade, 32)

    def test_timestamp(self):
        self.assertTrue(self.enrollment1.timestamp)
        self.assertEqual(self.enrollment2.timestamp, "2025-03-09")
