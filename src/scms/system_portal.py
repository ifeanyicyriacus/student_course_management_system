from django.core.validators import validate_email

def verify_administrator(administrator) -> bool:
    from scms.user_type import UserType
    return administrator.user_type == UserType.ADMINISTRATOR


class SystemPortal:
    user_id = 1
    def __init__(self):
        from scms.administrator import Administrator
        self.__users: list = []
        self.__courses: list = []
        administrator:Administrator = Administrator(str(0), "Portal Administrator", "admin@admin.com", "admin-password")
        self.__users.append(administrator)
    #     self.load_data()
    #     self = self

    @property
    def users(self):
        return self.__users

    @property
    def courses(self):
        return self.__courses

    def user_size(self):
        return len(self.__users)

    def course_size(self):
        return len(self.__courses)

    def register_user(self, fullname: str, email: str, password: str, user_type) -> None:
        from scms.user_type import UserType
        from scms.student import Student
        from scms.instructor import Instructor
        if user_type == UserType.STUDENT:
            self.__users.append(Student(str(self.user_id), fullname, email, password))
        else:
            self.__users.append(Instructor(str(self.user_id), fullname, email, password))
        self.user_id += 1

    def login(self, email: str, password: str):
        if validate_email and password is not None:
            user = self.__find_user_by_email(email)
            if user is not None:
                if user.authenticate_password(password):
                    return user
                else:
                    raise ValueError("Your credential doesn't match, try again")
            else:
                raise ValueError("User doesn't exist")

    def logout(self):
        # download object state
        pass

    def __find_user_by_email(self, email:str):
        for user in self.__users:
            if user.email == email:
                return user
        return None

    def remove_user(self, user, administrator):
        if user is None or administrator is None:
            raise ValueError("Valid User and Administrator is required")
        if verify_administrator(administrator):
            if user in self.__users: self.__users.remove(user)
            else: raise ValueError("User not found")
        else: raise ValueError("You don't have permission to remove this user")

    def get_users(self, user_type) -> list:
        return [user for user in self.__users if user.user_type == user_type]


