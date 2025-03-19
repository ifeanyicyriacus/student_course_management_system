import os

class FileHandler:
    def __init__(self, file_path):
        self.__set_file_path(file_path)

    def __set_file_path(self, file_path):
        self.__file_path = os.path.abspath(file_path)

    def write(self, content:str) -> None:
        try:
            with open(self.__file_path, 'a') as file:
                file.write(content+'\n')
        except FileNotFoundError:
            with open(self.__file_path, 'w') as file:
                file.write(content+'\n')

    def read(self) -> [str]:
        try:
            with open(self.__file_path, 'r') as file:
                return file.read().split('\n')[:-1]
        except FileNotFoundError:
            with open(self.__file_path, 'w') as file:
                file.write('')
            return self.read()

    def clear(self) -> None:
        with open(self.__file_path, 'w') as file:
            file.truncate(0)
