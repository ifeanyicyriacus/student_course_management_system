import unittest
from instructor import Instructor
from course import Course
from student import Student

class TestInstructor(unittest.TestCase):

    def test_create_course(self):
        instructor = Instructor(1, "John Doe", "john@example.com", "password123")
        course = Course("Python 101")
        instructor.create_course(course)
        self.assertIn(course, instructor.courses_taught)

    def test_view_students(self):
        instructor = Instructor(1, "John Doe", "john@example.com", "password123")
        course = Course("Python 101")
        student1 = Student("Alice")
        student2 = Student("Bob")
        course.students.append(student1)
        course.students.append(student2)
        instructor.create_course(course)




