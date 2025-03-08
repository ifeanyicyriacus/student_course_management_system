import abc
from src.scms.validator import Validator

class User(abc.ABC):
    __password = None
    def __init__(self, full_name: str, email: str, password: str):
        self.full_name = full_name
        self.email = email
        self._password = password

    @property
    def full_name(self) -> str:
        return self.__full_name

    @full_name.setter
    def full_name(self, full_name: str):
        if Validator.validate_input(full_name):
            self.__full_name = full_name
        else: raise ValueError("Invalid full name")

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        if Validator.validate_email(email):
            self.__email = email
        else: raise ValueError("Invalid email")

    @property
    def _password(self) -> str:
        return self.__password

    @_password.setter
    def _password(self, password: str):
        if Validator.validate_input(password):
            self.__password = password
        else: raise ValueError("Invalid password")

    def verify_password(self, password: str) -> bool:
        return Validator.validate_input(password) and password == self.__password

    def update_password(self, password: str, new_password: str) -> None:
        if self.verify_password(password):
            self._password = new_password
        else: raise ValueError("Incorrect password")

