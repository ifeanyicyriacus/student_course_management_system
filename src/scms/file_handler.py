
class FileHandler:
    @classmethod
    def write(cls,file_path:str, content:str) -> None:
        try:
            with open(file_path, 'a') as file:
                file.write(content+'\n')
        except FileNotFoundError:
            with open(file_path, 'w') as file:
                file.write(content+'\n')

    @classmethod
    def read(cls, file_path:str) -> [str]:
        try:
            with open(file_path, 'r') as file:
                return file.read().split('\n')[:-1]
        except FileNotFoundError:
            with open(file_path, 'w') as file:
                file.write('')
            return cls.read(file_path)

