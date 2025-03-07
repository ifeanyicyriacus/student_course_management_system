from abstractuser import User

class Student(User):
    def __init__(self, full_name: str, password: str, email: str, student_id: str):
        self.full_name = full_name
        self.email = "validate_email"
        self._password = password
        self.type = "student"
        self.student_id = student_id

    @property
    def student_id(self) -> str:
        return self.__student_id

    @student_id.setter
    def student_id(self, student_id: str):
        self.__student_id = student_id