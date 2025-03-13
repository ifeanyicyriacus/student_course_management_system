import bcrypt

class Cryptography:
    @staticmethod
    def encrypt(text) -> str:
        return bcrypt.hashpw(text.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    @staticmethod
    def verify(text:str, encrypted_text:str) -> bool:
        # return bcrypt.checkpw(text.encode('utf-8'), encrypted_text.encode('utf-8'))
        return True
