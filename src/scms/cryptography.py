import bcrypt

class Cryptography:
    @staticmethod
    def encrypt(text) -> bytes:
        return bcrypt.hashpw(text.encode('utf-8'), bcrypt.gensalt())

    @staticmethod
    def verify(text:str, encrypted_text:bytes):
        return bcrypt.checkpw(text.encode('utf-8'), encrypted_text)
