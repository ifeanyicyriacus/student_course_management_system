import re


def main_menu():
    current_user = None
    users = []

    while True:
        if current_user is None:
            print_line()
            print("Welcome to Student Course Management System.".center(150))
            print_line()
            user_input = input("""
            Kindly choose one of the options:
            1. Register as a new user
            2. Login to your account
            3. Exit the program
            """)
            if user_input == '1':
                new_buddy = register()
                users.append(new_buddy)
            elif user_input == '2':
                current_user = login(users)
            elif user_input == '3':
                print("Goodbye friend!")
            else:
                print("Invalid input. Try again.")
        else:
            print_line()
            print(f"Welcome back, {current_user['name']}!".center(150))
            print_line()
            choice = input("""
            Choose one of the options:
            1. Create a new course(facilitator only)
            2. Assign grades(facilitator only)
            3. Edit grades(facilitator only)
            4. View students enrolled in a course(facilitator only)
            5. Enroll in a course(student only)
            6. View your course(student only)
            7. Drop course(student only)
            8. View grades
            9. View your facilitator
            10. Manage your account
            11. Logout
            """)
            if choice == '1':
                create_course(current_user)
            elif choice == '2':
                assign_grades(current_user)
            elif choice == '3':
                edit_grades(current_user)
            elif choice == '4':
                view_students(current_user)
            elif choice == '5':
                enroll_course(current_user)
            elif choice == '6':
                view_courses(current_user)
            elif choice == '7':
                drop_course(current_user)
            elif choice == '8':
                view_grades(current_user)
            elif choice == '9':
                view_facilitator(current_user)
            elif choice == '10':
                manage_account(current_user)
            elif choice == '11':
                print("""
                Logged out...
                Logged out.
                """)
                current_user = None
            else:
                print("Invalid input. Try again.")


def print_line():
    print("====================================================================================================================================================")


def register():
    print("""
                                            *** Welcome To The Registration Zone ***

                            We're thrilled to have you join our community! Lets get you started! \U0001F60A
    """)
    email = input("Please enter your email: ")
    if not is_valid_email(email):
        return "Invalid email. Please enter a valid email address."

    name = input("""Great! Now, let's get your name.
    What's your full name?: 
    """).strip()
    password = input("Please enter your password: ").strip()
    role = input("Please enter your role(student/facilitator): ").strip().lower()
    available_roles = ["student", "facilitator"]
    if role not in available_roles:
        return ("""
        Please enter a valid role. You must enter student or facilitator.
        Try again.
        """)
    new_user = {"email": email, "password": password, "role": role, "name": name}
    print(f"\nYay! You've successfully registered, {name}! 🎉 You're all set up to explore!")
    return new_user


def login(users):
    print("Login to your account")
    email = input("Please enter your email: ").strip()
    if not is_valid_email(email):
        return "Invalid email. Please enter a valid email address."
    password = input("Please enter your password: ").strip()
    for user in users:
        if user["email"] == email and user["password"] == password:
            print(f"Login Successful! Welcome back, {user['name']}!")
            return user
        return "Login Failed! Invalid email or password!"



def is_valid_email(email):
    valid_email = re.match(r'^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2}$', email)
    if valid_email:
        return True
    return False



main_menu()



