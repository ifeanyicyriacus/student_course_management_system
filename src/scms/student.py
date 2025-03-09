from src.scms.user import User

class Student(User):
    def __init__(self, student_id: str, full_name: str, email: str, password: str):
        super().__init__(full_name, email, password)
        self.student_id = student_id

    @property
    def student_id(self) -> str:
        return self.__student_id

    @student_id.setter
    def student_id(self, student_id: str):
        from src.scms.validator import Validator
        if Validator.validate_input(student_id):
            self.__student_id = student_id
        else: raise ValueError("Student ID is not valid")