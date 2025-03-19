from src.scms.instructor import Instructor
from src.scms.portal import Portal
from src.scms.student import Student
from std_utility.io_function import print_line, clear_screen, input_int, exit_program, input_str, error_message, \
    input_email, info_message, success_message, input_password


def _confirm_change(prompt:str) -> bool:
    response = input_str(prompt)
    if response.lower() == 'yes': return True
    elif response.lower() == 'no': return False
    else:
        print(error_message("Invalid input. Please try again. only 'yes' or 'no' are supported"))
        return _confirm_change(prompt)


class ManageAccountMenu:
    def __init__(self, user:Student|Instructor, portal:Portal):
        self.user = user
        self._portal = portal

    def start(self):
        print_line()
        self.manage_account_menu("Manage Account Menu")

    def manage_account_menu(self, prompt:str):
        clear_screen()
        print_line()
        print("Welcome to the Manage Account Menu".center(50, "-"))
        print_line()

        menu_prompt = f"""
        Choose an option:
        1. Change your Fullname
        2. Change your Email
        3. Change your Password
        4. [<- go back to {("Student" if type(self.user) == Student else "Instructor" )} menu>]
        0. Exit
        """ + prompt + "\n>>>"
        choice = input_int(menu_prompt)
        match choice:
            case 1: self.change_user_fullname()
            case 2: self.change_email()
            case 3: self.change_password()
            case 4: pass
            case 0: exit_program()
            case _:
                self.manage_account_menu("Invalid selection: available options are (1 - 4 & 0) Try again")

    def change_user_fullname(self) -> None:
        if _confirm_change(f"Are you sure you want to change your Fullname from '{self.user.full_name}' yes/no?"):
            new_full_name = input("Enter a new fullname: ")
            self.user.full_name = new_full_name
            self.override_user_file()
            self.manage_account_menu(success_message("Fullname successfully changed to '{}'".format(self.user.full_name)))
        else:
            self.manage_account_menu(info_message("Fullname was not changed."))

    def change_email(self) -> None:
        if _confirm_change(f"Are you sure you want to change your Email from '{self.user.email}' yes/no?"):
            new_email = input_email()
            self.user.email = new_email
            self.override_user_file()
            self.manage_account_menu(success_message("Email successfully changed to '{}'".format(self.user.email)))
        else:
            self.manage_account_menu(info_message("Email was not changed."))

    def change_password(self):
        if _confirm_change(f"Are you sure you want to change your Password yes/no?"):
            current_password = input_password("Enter your current password: ")
            if self.user.verify_password(current_password):
                new_password = input("Enter new password: ")
                self.user.update_password(password=current_password, new_password=new_password)
                self.override_user_file()
            else:
                self.manage_account_menu(error_message("Wrong password, please try again."))
        else:
            self.manage_account_menu(info_message("Password was not changed."))

    def override_user_file(self):
        print(type(self.user))
        print(type(self.user) is Student)
        print(type(self.user) is Instructor)

        if type(self.user) is Student:
            print(type(self.user))
            self._portal.override_student_file()
        elif type(self.user) is Instructor:
            print(type(self.user))
            self._portal.override_instructor_file()
