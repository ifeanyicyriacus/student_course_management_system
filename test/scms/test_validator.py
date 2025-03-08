from unittest import TestCase
from src.scms.validator import Validator

class TestValidator(TestCase):
    def setUp(self):
        self.validator = Validator()

    def test_validate_email(self):
        self.assertTrue(self.validator.validate_email("adebayosamuel6667@gmail.com"))
        self.assertFalse(self.validator.validate_email("invalid-email"))

    def test_validate_input(self):
        self.assertTrue(self.validator.validate_input("my name"))
        self.assertFalse(self.validator.validate_input("   "))
        self.assertFalse(self.validator.validate_input(""))

