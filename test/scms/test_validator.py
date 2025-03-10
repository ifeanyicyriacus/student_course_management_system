from unittest import TestCase
from src.scms.validator import Validator


class TestValidator(TestCase):
    def setUp(self):
        self.validator = Validator()

    def test_validate_email(self):
        self.assertTrue(self.validator.validate_email("adebayosamuel6667@gmail.com"))
        self.assertFalse(self.validator.validate_email("invalid-email"))
        self.assertTrue(self.validator.validate_email("username@sub.sub.sub.domain.com"))
        self.assertTrue(self.validator.validate_email("chibuzo@domain.com.ng.lg"))
        self.assertTrue(self.validator.validate_email("ifeanyi.kehinde.onyinyechi@x.com"))

    def test_validate_input(self):
        self.assertTrue(self.validator.validate_input("my name"))
        self.assertFalse(self.validator.validate_input("   "))
        self.assertFalse(self.validator.validate_input(""))
        self.assertFalse(self.validator.validate_input(None))

    def test_validate_grade(self):
        self.assertTrue(self.validator.validate_grade("0"))
        self.assertTrue(self.validator.validate_grade("100"))
        self.assertFalse(self.validator.validate_grade("-1"))
        self.assertFalse(self.validator.validate_grade("101"))
        self.assertTrue(self.validator.validate_grade(0))
        self.assertTrue(self.validator.validate_grade(100))
        self.assertFalse(self.validator.validate_grade(-1))
        self.assertFalse(self.validator.validate_grade(101))

    def test_validate_password(self):
        self.assertFalse(self.validator.validate_password("<PASSWORD>"))
        self.assertFalse(self.validator.validate_password("123456789"))
        self.assertFalse(self.validator.validate_password("asdfghjkl"))
        self.assertFalse(self.validator.validate_password("ASDFGHJKL"))
        self.assertFalse(self.validator.validate_password("         "))
        self.assertFalse(self.validator.validate_password("~!@#$%^&*()_+"))
        self.assertFalse(self.validator.validate_password("pAsSw OrD"))
        self.assertFalse(self.validator.validate_password("PaSsWoRd1"))
        self.assertTrue(self.validator.validate_password("$<PaSsWoRd123>%"))
        self.assertTrue(self.validator.validate_password("PaSs  WoRd1"))
