from scms.user import User
import bcrypt

class Cryptography(User):
    @staticmethod
    def encrypt(text) -> str:
        return str(bcrypt.hashpw(text.encode9('utf-8'), bcrypt.gensalt()))

    @staticmethod
    def verify(text:str, encrypted_text:str) -> bool:
        return bcrypt.checkpw(text.encode('utf-8'), encrypted_text.encode('utf-8'))
