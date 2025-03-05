from abc import ABC
from scms.user_type import UserType

class User(ABC):
    def __init__(self, user_id:str, full_name:str, email:str, password:str, user_type:UserType):
        self.__USER_ID = user_id
        self.full_name = full_name
        self.email = email
        self._password = password
        self.user_type = user_type

    @property
    def user_id(self) -> str:
        return self.__USER_ID

    @property
    def full_name(self) -> str:
        return self.__full_name
    @full_name.setter
    def full_name(self, full_name:str):
        self.__full_name = full_name

    @property
    def email(self) -> str:
        return self.__email
    @email.setter
    def email(self, email:str):
        self.__email = email

    @property
    def _password(self) -> str:
        return self.__password
    @_password.setter
    def _password(self, password:str):
        self.__password = password

    @property
    def user_type(self) -> UserType:
        return self.__user_type
    @user_type.setter
    def user_type(self, user_type:UserType):
        self.__user_type = user_type

    def change_password(self, old_password:str, new_password:str):
        if self._authenticate_password(old_password): self._password = new_password
        else: raise ValueError("Wrong password, try again")

    def _authenticate_password(self, password) -> bool:
        return self._password == password
