from scms.manager import CourseManager
from scms.user import User, UserType
from scms.course import Course


class Instructor(User, CourseManager):
    def __init__(self, user_id:str, full_name:str, email:str, password:str):
        super().__init__(
            user_id,
            full_name,
            email,
            password,
            UserType.INSTRUCTOR
        )

        self.__assigned_course:[Course] = []

