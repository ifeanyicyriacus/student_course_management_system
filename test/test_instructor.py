from unittest import TestCase
from instructor import Instructor
from course import Course
from student import Student

class TestInstructor(TestCase):

    def test_create_course(self):
        instructor = Instructor(1, "adebayo kehinde", "adebayosamuel6667@gmail.com", "password123")
        course = Course("Python 101")
        instructor.create_course(course)
        self.assertIn(course, instructor.courses_taught)

    def test_view_students(self):
        instructor = Instructor(1, "adebayo", "adebayosamuel6667@gmail.com", "password123")
        course = Course("Python ")
        student1 = Student("samuel")
        student2 = Student("ayo")
        course.students.append(student1)
        course.students.append(student2)
        instructor.create_course(course)




