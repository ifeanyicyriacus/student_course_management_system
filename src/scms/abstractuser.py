from validator import Validator
class User(Validator):
    def __init__(self, full_name: str, password: str, email: str, type: str):
        self.full_name = full_name
        self.email = email
        self._password = password
        self.user_type = type

    @property
    def full_name(self) -> str:
        return self.__full_name

    @full_name.setter
    def full_name(self, full_name: str):
        self.__full_name = full_name

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def _password(self) -> str:
        return self.__password

    @_password.setter
    def _password(self, password: str):
        self.__password = password

    @property
    def type(self) -> str:
        return self.__user_type

    @type.setter
    def type(self, type: str):
        self.__user_type = type


