
from scms.user import User, UserType

class Student(User):
    def __init__(self, student_id, full_name, email, password):
        super().__init__(
            student_id,
            full_name,
            email,
            password,
            UserType.STUDENT
        )
        self.__enrolled_course:list = []

    def enroll(self, course) -> None:

        pass

    def drop(self, course) -> None:

        pass

    def view_grades(self) -> list:

        pass

