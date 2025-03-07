import re
import sys
from scms.student import Student
from scms.instructor import Instructor


class Portal:

    def __init__(self):
        self.users = []


    def register(self):
        print("""
                                            *** Welcome To The Registration Zone ***

                            We're thrilled to have you join our community! Lets get you started! \U0001F60A
        """)
        email = input("Please enter your email: ")
        if self.find_user_by_email(email):
            email_again = input("""
            Email Already Registered!
            Enter another email
            """)
        else:
            name = input("""Great! Now, let's get your name.
            What's your full name?: 
            """).strip()
            password = input("Please enter your password: ").strip()
            confirm_password = input("Confirm password: ").strip()
            if password != confirm_password:
                input_password_again = input("""
                Passwords don't match.
                Please enter your password again: 
                """)
            else:
                role = input("""
                Are you a:
                1. Student
                2. Instructor
                """).strip().lower()
                available_roles = ["student", "instructor"]
                if role not in available_roles:
                    return ("""
                    Please enter a valid role. You must enter student(1) or instructor(2).
                    Try again.
                    """)
                if role == "student".lower():
                    new_buddy = Student(email, name, password, role)
                elif role == "instructor".lower():
                    new_buddy = Instructor(email, name, password, role)
                else:
                    print("Invalid role.")
                self.users.append(new_buddy)
                new_buddy = {"email": email, "password": password, "role": role, "name": name}
                print(f"\nYay! You've successfully registered, {name}! 🎉 Now you can login!")
            return new_buddy


    def login(self, users):
        print("Login to your account")
        email = input("Please enter your email: ").strip()
        # if not is_valid_email(email):
        # return "Invalid email. Please enter a valid email address."
        password = input("Please enter your password: ").strip()
        for user in users:
            if user["email"] == email and user["password"] == password:
                print(f"Login Successful! Welcome back, {user['name']}!")
                return user
            return "Login Failed! Invalid email or password!"


    def add_user(self, new_buddy):
        self.users.append(new_buddy)

    def find_user_by_email(self, email):
        for user in self.users:
            if user.email == email:
                return user



class MainMenu:
    def __init__(self):
        self.portal = Portal()
        self.current_user = None
        self.users = []



    def main_menu(self, role):
        # users = []

        while True:
            if self.current_user is None:
                self.print_line()
                print("Welcome to Student Course Management System.".center(150))
                self.print_line()
                user_input = input("""
                Kindly choose one of the options:
                1. Register as a new user
                2. Login to your account
                3. Exit the program
                """)
                if user_input == '1':
                    new_buddy = self.portal.register()
                elif user_input == '2':
                    self.current_user = self.portal.login(self.users)
                    # self.portal.add_user(new_buddy)
                    if role == 1:
                        self.student_dashboard()
                    elif role == 2:
                        self.instructor_dashboard(self)
                elif user_input == '3':
                    print("Goodbye friend!")
                else:
                    print("Invalid input. Try again.")



    def student_dashboard(self):
        while True:
            self.print_line()
            print("Welcome to Student Dashboard".center(150))
            self.print_line()
            reply = input("""
            Choose one of the options:
            1.Enroll in a course
            2.View your courses
            3.View grades
            4.View your instructor
            5.Manage your account
            6.Logout
            """)
            if reply == '1':
                self.student.enroll_course(self)
            elif reply == '2':
                self.student.view_course(self)
            elif reply == '3':
                self.student.view_grades(self)
            elif reply == '4':
                self.student.view_instructor(self)
            elif reply == '5':
                self.student.manage_account(self)
            elif reply == '6':
                sys.exit()
            else:
                return "Invalid input. Try again."

    def instructor_dashboard(self, self1):
        while True:
            self.print_line()
            print("Welcome to Instructor Dashboard".center(150))
            self.print_line()
            decision = input("""
            Choose one of the options:
            1. Create a new course
            2. Assign grades
            3. Edit grades
            4. View students enrolled in a course
            5. Logout
            """)
            if decision == '1':
                self.instructor.create_course(self)
            elif decision == '2':
                self.instructor.assign_grades(self)
            elif decision == '3':
                self.instructor.edit_grades(self)
            elif decision == '4':
                self.instructor.view_enrolled_students(self)
            elif decision == '5':
                self.current_user = None
                sys.exit()
            else:
                return "Invalid input. Try again."



    def print_line(self):
        print("====================================================================================================================================================")

    # def is_valid_email(email):
    #     valid_email = re.match(r'^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2}$', email)
    #         if email is not valid_email:
    #             return False
    #         return True


MainMenu().main_menu(2)








