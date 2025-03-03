def print_line():
    print("========================================================")


def register():
    print("""
    *** Welcome To The Registration Zone ***
    
    We're thrilled to have you join our community! Lets get you started! \U0001F60A
    """)
    email = input("Please enter your email: ")

    name = input("""Great! Now, let's get your name.
    What's your full name?: 
    """).strip()
    password = input("Please enter your password: ").strip()
    role = input("Please enter your role(student/facilitator): ").strip().lower()
    available_roles = ["student", "facilitator"]
    if role not in available_roles:
        return("""
        Please enter a valid role. You must enter student or facilitator.
        Try again.
        """)
    new_user = {"email": email, "password": password, "role": role, "name": name}
    print(f"\nYay! You've successfully registered, {name}! 🎉 You're all set up to explore!")
    return new_user



def login(users):
    print("Login to your account")
    email = input("Please enter your email: ").strip()
    password = input("Please enter your password: ").strip()
    for user in users:
        if user["email"] == email and user["password"] == password:
            print("Login Successful! Welcome back, {user['name']}!")
            return user
        return "Login Failed! Invalid email or password!"



def main_menu():


    current_user = None
    users = []

    while True:
        if current_user:
            print_line()
            print("Welcome to Student Course Management System.")
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

main_menu()



