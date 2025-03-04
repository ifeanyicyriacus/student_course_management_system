from abc import ABC, abstractmethod
from enum import Enum


class UserType(Enum):
    INSTRUCTOR = "INSTRUCTOR"
    STUDENT = "STUDENT"
    ADMINISTRATOR = "ADMINISTRATOR"


class User(ABC):
    def __init__(self, user_id:str, full_name:str, email:str, password:str, user_type:UserType):
        self.user_id = user_id
        self.full_name = full_name
        self.email = email
        self.password = password
        self.user_type = user_type

        @abstractmethod
        def login(self, email:str, password:str):
            pass

        @abstractmethod
        def logout(self):
            pass

        def reset_password(self):
            print("Password reset logic here")