from scms.course_manager import CourseManager
from scms.user import User, UserType
from scms.course import Course


class Instructor(User, CourseManager):
    def __init__(self, instructor_id:str, full_name:str, email:str, password:str):
        super().__init__(
            instructor_id,
            full_name,
            email,
            password,
            UserType.INSTRUCTOR
        )
        self.__assigned_course:[Course] = []

    def assign_grade(self, student, course, grade_value: str):
        pass

    def view_enrolled_students(self, course) -> list:
        pass

    def create_course(self, course_id:str, course_name:str, course_description:str):
        pass

    def delete_course(self, course_id:str):
        pass