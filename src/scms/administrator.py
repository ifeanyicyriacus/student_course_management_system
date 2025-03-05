# from scms.user_manager import UserManager
# from scms.course_manager import CourseManager
from scms.user import User, UserType
#
#
# class Administrator(User, UserManager, CourseManager):
class Administrator(User):
    def __init__(self, user_id = "0",
            full_name = "Super Administrator",
            email = "admin@admin.com",
            password = "admin-password",
            user_type = UserType.ADMINISTRATOR):
        super().__init__(
            user_id = user_id,
            full_name = full_name,
            email = email,
            password = password,
            user_type = user_type
        )
#
#     def add_user(self, user):
#         pass
#
#     def remove_user(self, user):
#         pass
#
#
#     def create_course(self, course_id:str, course_name:str, course_description:str):
#         pass
#
#     def delete_course(self, course_id:str):
#         pass
#
