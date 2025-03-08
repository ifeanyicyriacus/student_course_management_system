from unittest import TestCase
from src.scms.abstractuser import User

class TestUser(TestCase):
    def setUp(self):
        self.user = User(full_name="Adebayo kehinde", password="user123", email="adebayosamuel6667@gmail.com", type="instructor")

    def test_full_name(self):
        self.assertEqual(self.user.full_name, "Adebayo kehinde")
        self.user.full_name = "Adebayo kehinde"
        self.assertEqual(self.user.full_name, "Adebayo kehinde")

    def test_email(self):
        self.assertEqual(self.user.email, "adebayosamuel6667@gmail.com")
        self.user.email = "adebayosamuel6667@gmail.com"
        self.assertEqual(self.user.email, "adebayosamuel6667@gmail.com")

    def test_password(self):
        self.assertEqual(self.user._password, "user123")
        self.user._password = "user123"
        self.assertEqual(self.user._password, "user123")

    def test_user_type(self):
        self.assertEqual(self.user.user_type, "instructor")
        self.user.user_type = "instructor"
        self.assertEqual(self.user.user_type, "instructor")


