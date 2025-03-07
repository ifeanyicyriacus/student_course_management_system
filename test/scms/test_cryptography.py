import unittest
from src.scms.cryptography import Cryptography

class TestCryptography(unittest.TestCase):
    def test_encrypt(self):
        encrypted_txt = Cryptography.encrypt("hello")
        self.assertTrue(Cryptography.verify("hello", encrypted_txt))

    def test_that_verify_returns_correct_password(self):
        is_correct = Cryptography.verify("hello", Cryptography.encrypt("hello"))
        self.assertTrue(is_correct)

    def test_verify_returns_false_for_incorrect_password(self):
        incorrect_txt = Cryptography.encrypt("incorrect password")
        self.assertFalse(Cryptography.verify("hello", incorrect_txt))

