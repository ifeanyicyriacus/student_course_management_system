from scms.user_manager import UserManager
from scms.course_manager import CourseManager
from scms.user import User, UserType


class Administrator(User, UserManager, CourseManager):
    def __init__(self):
        super().__init__(
            user_id = "0",
            full_name = "Administrator",
            email = "super_admin@gmail.com",
            password = "<PASSWORD>",
            user_type = UserType.ADMINISTRATOR
        )

    def add_user(self, user):
        pass

    def remove_user(self, user):
        pass


    def create_course(self, course_id:str, course_name:str, course_description:str):
        pass

    def delete_course(self, course_id:str):
        pass

