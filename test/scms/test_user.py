from unittest import TestCase
from src.scms.user import User

class TestUser(TestCase):
    full_name = "Adebayo kehinde"
    password = "123"
    email = "adebayosamuel6667@gmail.com"
    empty_value = ""

    def setUp(self):
        self.user = User(self.full_name, self.email, self.password)

    def test_full_name(self):
        self.assertEqual(self.user.full_name, self.full_name)
        self.user.full_name = "Adebayo kehinde Taiwo"
        self.assertEqual(self.user.full_name, "Adebayo kehinde Taiwo")

    def test_email(self):
        self.assertEqual(self.user.email, self.email)
        self.user.email = "new.email@semicolon.com"
        self.assertEqual(self.user.email, "new.email@semicolon.com")

    def test_password(self):
        self.assertTrue(self.user.verify_password(self.password))
        self.assertFalse(self.user.verify_password("wrong_password"))

    def test_update_password(self):
        self.assertTrue(self.user.verify_password(self.password))
        self.user.update_password(self.password, "<NEW_PASSWORD>")
        self.assertTrue(self.user.verify_password("<NEW_PASSWORD>"))

    def test_setting_invalid_field_value_raises_error(self):
        with self.assertRaises(ValueError):
            self.new_user = User(self.empty_value, self.email, self.password)
            self.new_user = User(self.full_name, self.empty_value, self.password)
            self.new_user = User(self.full_name, self.email, self.empty_value)
        with self.assertRaises(ValueError):
            self.user.full_name = self.empty_value
        with self.assertRaises(ValueError):
            self.user.email = self.empty_value
        with self.assertRaises(ValueError):
            self.user._password = self.empty_value
        with self.assertRaises(ValueError):
            self.user.update_password(self.password, self.empty_value)