from datetime import date

from src.scms.validator import Validator


class Enrollment:
    def __init__(self, course_id:str, student_id:str, grade:int|str = 0, timestamp:str = str(date.today().isoformat())):
        self.course_id = course_id
        self.student_id = student_id
        self.grade = grade
        self.__TIMESTAMP:str = timestamp

    @property
    def course_id(self) -> str:
        return self.__course_id
    @course_id.setter
    def course_id(self, course_id: str):
        if Validator.validate_input(course_id):
            self.__course_id = course_id
        else: raise ValueError("Invalid course_id")

    @property
    def student_id(self) -> str:
        return self.__student_id
    @student_id.setter
    def student_id(self, student_id: str):
        if Validator.validate_input(student_id):
            self.__student_id = student_id
        else: raise ValueError("Invalid student_id")

    @property
    def grade(self) -> int:
        return self.__grade
    @grade.setter
    def grade(self, grade: str|int):
        if Validator.validate_grade(grade):
            self.__grade = int(grade)
        else: raise ValueError("Invalid grade")

    @property
    def timestamp(self) -> str:
        return self.__TIMESTAMP
