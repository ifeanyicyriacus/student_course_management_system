from scms.instructor import Instructor
from scms.portal import Portal
from scms.student import Student
from std_utility.io_function import print_line, clear_screen, input_int, exit_program, input_str


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

    def change_user_fullname(self):
        current_password = input_str("Enter your current password: ")
        if self._portal.verify_user_password(self.user, current_password):
            new_fullname = input_str("Enter your new fullname: ")
            self.user.fullname = new_fullname
            self._portal.update_user(self.user)
            print("Fullname updated successfully.")
        else:
            print("Incorrect password.")

    def change_email(self):
        current_password = input_str("Enter your current password: ")
        if self._portal.verify_user_password(self.user, current_password):
            new_email = input_str("Enter your new email: ")
            self.user.email = new_email
            self._portal.update_user(self.user)
            print("Email updated successfully.")
        else:
            print("Incorrect password.")

        pass

    def change_password(self):
        # ask for current password
        updated_user = self.user
        # enter your current password
        # enter new password
        self._portal.update_User(updated_user)
        pass
