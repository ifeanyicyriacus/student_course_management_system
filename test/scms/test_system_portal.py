import unittest
from text_format.trash.system_portal import SystemPortal
from text_format.trash.user_type import UserType


class SystemPortalTestCase(unittest.TestCase):
    empty_list:list = []
    full_name = "full_name"
    email = "email"
    admin_email = "admin@admin.com"
    wrong_email = "wrong_email"
    password = "password"
    admin_password = "admin-password"
    wrong_password = "wrong-password"

    def setUp(self):
        self.system_portal = SystemPortal()

    def test_system_portal_is_life_and_active(self):
        self.assertListEqual(self.system_portal.courses, self.empty_list)
        self.assertEqual(self.system_portal.user_size(), 1)
        self.assertEqual(self.system_portal.course_size(), 0)

    def test_system_portal_has_an_administrator_after_creation(self):
        self.assertEqual(self.system_portal.user_size(), 1)
        portal_admin = self.system_portal.login(self.admin_email, self.admin_password)
        self.assertEqual(portal_admin.user_type, UserType.ADMINISTRATOR)
        self.assertTrue(portal_admin.authenticate_password(self.admin_password))

    def test_system_portal_can_be_used_to_register_student(self):
        self.assertEqual(self.system_portal.user_size(), 1)
        self.system_portal.register_user(self.full_name, self.email, self.password, UserType.STUDENT)
        self.assertNotEqual(self.system_portal.users, self.empty_list)
        self.assertEqual(self.system_portal.user_size(), 2)

    def test_that_system_portal_can_be_used_to_login_existing_student_with_valid_credential(self):
        self.assertEqual(self.system_portal.user_size(), 1)
        self.system_portal.register_user(self.full_name, self.email, self.password, UserType.STUDENT)
        self.assertEqual(self.system_portal.user_size(), 2)

        login_user = self.system_portal.login(self.email, self.password)
        self.assertEqual(login_user.full_name, self.full_name)
        self.assertEqual(login_user.email, self.email)

    def test_that_system_portal_raise_exception_with_invalid_credential(self):
        self.assertEqual(self.system_portal.user_size(), 1)
        self.system_portal.register_user(self.full_name, self.email, self.password, UserType.STUDENT)
        self.assertEqual(self.system_portal.user_size(), 2)

        with self.assertRaises(ValueError):
            self.system_portal.login(self.email, self.wrong_password)
        with self.assertRaises(ValueError):
            self.system_portal.login(self.wrong_email, self.password)
        with self.assertRaises(ValueError):
            self.system_portal.login(self.wrong_email, self.wrong_password)





