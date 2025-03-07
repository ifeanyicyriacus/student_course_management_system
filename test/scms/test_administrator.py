import unittest

from text_format.trash.system_portal import SystemPortal
from text_format.trash.user import User
from text_format.trash.user_type import UserType


class AdministratorTestCase(unittest.TestCase):
    full_name = "full_name"
    email = "email"
    admin_email = "admin@admin.com"
    wrong_email = "wrong_email"
    password = "password"
    admin_password = "admin-password"
    wrong_password = "wrong-password"

    def setUp(self):
        self.system_portal = SystemPortal()

    def test_administrator_can_remove_user(self):
        administrator = self.system_portal.login(self.admin_email, self.admin_password)
        self.assertTrue(administrator)
        self.assertEqual(1, self.system_portal.user_size())
        self.system_portal.register_user(self.full_name, self.email, self.password, UserType.STUDENT)
        self.assertEqual(2, self.system_portal.user_size())
        user:User = self.system_portal.login(self.email, self.password)
        self.assertTrue(user)
        self.system_portal.remove_user(user, administrator)
        self.assertEqual(1, self.system_portal.user_size())

    def test_administrator_can_view_all_user(self):
        all_admin = self.system_portal.get_users(UserType.ADMINISTRATOR)
        self.assertEqual(1, len(all_admin))
        all_student = self.system_portal.get_users(UserType.STUDENT)
        self.assertListEqual([], all_student)
        all_instructor = self.system_portal.get_users(UserType.INSTRUCTOR)
        self.assertListEqual([], all_instructor)
        all_users = self.system_portal.users
        self.assertEqual(1, len(all_users))

        self.system_portal.register_user(self.full_name, self.email, self.password, UserType.STUDENT)
        self.assertEqual(1, len(self.system_portal.get_users(UserType.STUDENT)))
        self.system_portal.register_user(self.full_name, self.email, self.password, UserType.INSTRUCTOR)
        self.assertEqual(1, len(self.system_portal.get_users(UserType.INSTRUCTOR)))
        self.assertEqual(3, len(self.system_portal.users))



