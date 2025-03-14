from scms.manage_account_menu import ManageAccountMenu
from src.scms.course import Course
from src.scms.portal import Portal
from src.scms.student import Student
from src.std_utility.ui_styling import StringFormatting
from src.std_utility.io_function import Validator, input_str, clear_screen, error_message, input_int, exit_program, \
    print_line, input_course_id
from std_utility.io_function import info_message, success_message


class StudentMenu:
    def __init__(self, student:Student, portal:Portal):
        self._student:Student = student
        self._portal:Portal = portal

    def start(self):
        print_line()
        self.student_menu(f"Student Login Successful! Welcome back, {self._student.full_name}!", )

    def student_menu(self, prompt: str) -> None:
        clear_screen()
        print_line()
        print("Welcome to Student Dashboard".center(150, "-"))
        print_line()

        menu_prompt = """
        Choose one of the options:
        1.Enroll in a course
        2.View my courses
        3.View my grades
        4.View my instructor
        5.Manage your account
        6.Logout
        0.Exit

        """ + prompt + "\n>>>"
        choice = input_int(menu_prompt)
        match choice:
            case 1: self.enroll_in_course()
            case 2: self.view_my_courses()
            case 3: self.view_my_grades()
            case 4: self.view_my_instructor()
            case 5: ManageAccountMenu(self._student, self._portal).start()
            case 6: pass
            case 0: exit_program()
            case _:
                self.student_menu(error_message("Invalid selection: available options are (1 - 6 & 0) Try again"))

    def enroll_in_course(self):
        print("Enroll in a course")
        if len(self._portal.courses) == 0:
            self.student_menu(info_message("No course available. Please try again later."))
        else:
            StringFormatting(f"{"Course-ID":>10} | {"Course Name":<15}").bold().underline().print()
            for course in self._portal.courses:
                print(f"{course.course_id:>10} | {course.course_name:<15}")

            course_id = input_course_id()
            valid_course_id:str = ""
            try:
                for course in self._portal.courses:
                    if course_id.upper() == course.course_id.upper():
                        valid_course_id = course.course_id.upper()
                        break
                self._portal.add_enrollment(valid_course_id, self._student.student_id)
                self.student_menu(info_message("Enrollment successful!"))
            except ValueError:
                self.student_menu(error_message("CourseID not associated with any existing course."))


    def view_my_courses(self):
        # fetch all courses
        # for there student_id == self._portal
    #     my_courses = self.portal.get_course_by(student_id)
        # display_courses(my_courses)//course id and name
        pass

    def view_my_grades(self):
        # my_enrollments = self.portal.get_enrollment_by_student_id()
        # display_enrollments(my_enrollments) //course_id | course_id

        # after displaying "show, a simple press enter to continue"
        # input_escape("press enter to continue") used as a pause anything goes
        pass

    def view_my_instructor(self):
        #  course | instructors
        #
        pass

    def manage_account(self):

        pass

def display_courses(courses: [Course]) -> str:
    text = StringFormatting("Courses:\n").underline().bold().green()
    text += StringFormatting(f'{"ID":>10} - {"NAME":>20}\n').bold()
    for course in courses:
        text += f"{course.course_id} - {course.course_name}\n"
    return text


