# from unittest import TestCase
# from src.scms.instructor import Instructor
# from src.scms.course import Course
# from src.scms.student import Student
#
#
# class TestCourse(TestCase):
#     def setUp(self):
#         self.instructor = Instructor('001', 'adebayo', 'adebayosamuel6667@gmail.com', 'password123')
#         self.course = Course('1234', 'Computer Science', 'Introduction to Computer Science', self.instructor)
#         self.student = Student('123', 'adebayo kehinde')
#
#     def test_enroll_student(self):
#         self.course.enroll_student(self.student)
#         self.assertIn(self.student, self.course.students)
#         self.assertIn(self.student.user_id, self.course.grades)
#         self.assertEqual(self.course.grades[self.student.user_id], None)
#
