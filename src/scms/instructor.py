from src.scms.user import User

class Instructor(User):
    def __init__(self, instructor_id:str, full_name:str, email:str, password:str):
        super().__init__(full_name, email, password)
        self.instructor_id = instructor_id

    @property
    def instructor_id(self) -> str:
        return self.__instructor_id

    @instructor_id.setter
    def instructor_id(self, instructor_id:str):
        from src.scms.validator import Validator
        if Validator.validate_input(instructor_id):
            self.__instructor_id = instructor_id
        else: raise ValueError("Instructor ID is not valid")