from unittest import Testcase
import student
import validator

class Teststudent(Testcase):

    def test_setUp(self,):
        self.Student = student(self, fullname = "adebayo kehinde", password = "1234", email = "adebaosamuel6667@gmail.com")