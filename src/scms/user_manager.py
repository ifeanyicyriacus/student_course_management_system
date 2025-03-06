from abc import ABC, abstractmethod

class UserManager(ABC):
    @abstractmethod
    def add_user(self, user):
        pass

    @abstractmethod
    def remove_user(self, user):
        pass