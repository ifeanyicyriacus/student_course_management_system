from src.scms.instructor import Instructor
from src.scms.manage_account_menu import ManageAccountMenu
from src.scms.course import Course
from src.scms.portal import Portal
from src.scms.student import Student
from src.std_utility.ui_styling import StringFormatting
from src.std_utility.io_function import Validator, input_str, clear_screen, error_message, input_int, exit_program, \
    print_line, input_course_id, score_to_grade
from src.std_utility.io_function import info_message, success_message


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
        StringFormatting("Enroll in a course").bold().print()
        if len(self._portal.courses) == 0:
            self.student_menu(info_message("No course available. Please try again later."))
        else:
            count = 1
            StringFormatting(f"{"s/n":>3} | {"Course-ID":>10} | {"Course Name":<15}").bold().underline().print()
            for course in self._portal.courses:
                print(f"{count:>3} | {course.course_id:>10} | {course.course_name:<15}")
                count += 1
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
        StringFormatting("My Courses:").bold().print()
        courses = self._portal.get_courses_by(self._student.student_id)

        if len(courses) == 0:
            self.student_menu(info_message("You are not enrolled in any courses."))
        else:
            count = 1
            StringFormatting(f"{"s/n":>3} | {"Course-ID":>10} | {"Course Name":<15}").bold().underline().print()
            for course in courses:
                print(f"{count:>3} | {course.course_id:>10} | {course.course_name:<15}")
                count += 1
        print(info_message(f"You are enrolled to {len(courses)} courses."))
        input("press enter to continue...")
        self.student_menu("Welcome back to your menu!")

    def view_my_grades(self):
        count = 1
        passes = 0
        fails = 0
        ungraded = 0
        StringFormatting("My Grades:").bold().print()
        my_grades:list = self._portal.get_courses_and_grades_by(self._student.student_id)
        if len(my_grades) == 0:
            self.student_menu(info_message("You are not enrolled in any courses."))
        else:
            StringFormatting(f"{"s/n":>3} | {"Course Name":<15} | {"Grade":<4}").bold().underline().print()
            for grade in my_grades:
                print(f"{count:>3} | {grade["course_name"]:<15} | {"un-graded" if (grade["grade"] == 0) else score_to_grade(grade["grade"]):<4}")
                count += 1
                if grade["grade"] >= 50: passes += 1
                elif grade["grade"] == 0: ungraded += 1
                else: fails += 1

        (StringFormatting(f"You are enrolled in {len(my_grades)} courses.").bold().br()
                       .append(f"Passes: {passes}").green().br()
                       .append(f"Fails: {fails}").red().br()
                       .append(f"Ungraded: {ungraded}").yellow().br().print())

        input("press enter to continue...")
        self.student_menu("Welcome back to your menu!")


    def view_my_instructor(self):
        my_courses: [Course]
        my_instructors: [Instructor]
        my_courses, my_instructors = self._portal.get_courses_and_instructors_by(self._student.student_id)

        counter = 1
        for my_instructor in my_instructors:
            StringFormatting(f"\n{counter:>2}. {my_instructor.full_name:<15}").underline().bold().print()
            counter += 1
            for course in my_courses:
                if course.instructor_id == my_instructor.instructor_id:
                    StringFormatting(f"   o {course.course_name:<15}").italic().print()
        input("press enter to continue...")
        self.student_menu("Welcome back to your menu!")

    def manage_account(self):
        ManageAccountMenu(self._student, self._portal).start()
        self.student_menu("Welcome back to your menu!")

# def display_courses(courses: [Course]) -> str:
#     text = StringFormatting("Courses:\n").underline().bold().green()
#     text += StringFormatting(f'{"ID":>10} - {"NAME":>20}\n').bold()
#     for course in courses:
#         text += f"{course.course_id} - {course.course_name}\n"
#     return text




