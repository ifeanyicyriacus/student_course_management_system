from src.scms.student import Student
from src.scms.course import Course
from src.scms.manage_account_menu import ManageAccountMenu
from src.scms.instructor import Instructor
from src.scms.portal import Portal
from std_utility.io_function import input_int, error_message, clear_screen, print_line, exit_program, input_str, \
    success_message, input_course_id, input_student_id, info_message, input_score
from std_utility.ui_styling import StringFormatting


class InstructorMenu:
    def __init__(self, instructor:Instructor, portal:Portal):
        self._instructor = instructor
        self._portal = portal

    def start(self):
        self.instructor_menu(f"Instructor Login Successful! Welcome back, {self._instructor.full_name}!")

    def instructor_menu(self, prompt:str) -> None:
        clear_screen()
        print_line()
        print("Welcome to Instructor Dashboard".center(150, "-"))
        print_line()

        menu_prompt = """
        Choose one of the options:
        1. Create a new course
        2. Assign grades
        3. View students enrolled in my course
        4. Manage your account
        5. Logout
        0. Exit

        """ + prompt + "\n>>>"
        choice = input_int(menu_prompt)
        match choice:
            case 1: self.create_new_course()
            case 2: self.assign_grades()
            case 3: self.view_students_enrolled_in_my_course()
            case 4: ManageAccountMenu(self._instructor, self._portal).start()
            case 5: pass
            case 0: exit_program()
            case _:
                self.instructor_menu(error_message("Invalid selection: available options are (1 - 5 & 0) Try again"))

    def create_new_course(self):
        course_name:str = input_str("Enter course name: ")
        course_description:str = input_str("Enter course description: ")
        instructor_id:str = self._instructor.instructor_id
        try:
            self._portal.add_course(course_name, course_description, instructor_id)
            self.instructor_menu(success_message(f"You have successfully created {course_name}!"))
        except ValueError as e:
            print(error_message("Course not added. Please try again."))
            self.create_new_course()

    def assign_grades(self):
        my_courses:[Course] = self._portal.get_instructors_course_by(self._instructor.instructor_id)

        clear_screen()
        count = 1
        StringFormatting(f"{"s/n":>3} | {"Course-ID":>10} | {"Course Name":<15}").bold().underline().print()
        for course in self._portal.courses:
            print(f"{count:>3} | {course.course_id:>10} | {course.course_name:<15}")
            count += 1
        course_id = input_course_id()
        clear_screen()
        valid_course_id: str = ""
        course_name:str = ""
        try:
            for course in my_courses:
                if course_id.upper() == course.course_id.upper():
                    valid_course_id = course.course_id.upper()
                    course_name = course.course_name
                    break
            if valid_course_id == "":
                raise ValueError
        except ValueError:
            self.instructor_menu(error_message("CourseID not associated with any existing course."))

        my_students:[Student] = self._portal.get_student_enrolled_in(course_id=course_id)

        StringFormatting(f"Student offering {course_name} are: ").underline().bold().print()
        StringFormatting(f"{"s/n":>3} | {"Student-ID":>10} | {"Student Name":>15}").underline().bold().print()
        count = 1
        for student in my_students:
            StringFormatting(f"{count:>3} | {student.student_id:>10} | {student.full_name}").underline().print()
            count += 1

        student_id = input_student_id()
        clear_screen()
        valid_student_id: str = ""
        student_full_name:str = ""
        try:
            for student in my_students:
                if student_id.upper() == student.student_id.upper():
                    valid_student_id = student.student_id.upper()
                    student_full_name = student.full_name
                    break
            if valid_student_id == "":
                raise ValueError
        except ValueError:
            self.instructor_menu(error_message("StudentID not associated with any existing student."))

        student_grade = input_score(f"Enter score for Student {student_full_name} ({valid_student_id})")
        try:
            self._portal.score_student(student_id=student_id, course_id=course_id, score=student_grade)
            self.instructor_menu(success_message(f"You have successfully scored {student_full_name}!"))
        except ValueError as e:
            self.instructor_menu(error_message(f"Unable to score, {str(e)}. Please try again."))

    def view_students_enrolled_in_my_course(self):
        my_courses: [Course] = self._portal.get_instructors_course_by(self._instructor.instructor_id)

        clear_screen()
        count = 1
        StringFormatting(f"{"s/n":>3} | {"Course-ID":>10} | {"Course Name":<15}").bold().underline().print()
        for course in self._portal.courses:
            print(f"{count:>3} | {course.course_id:>10} | {course.course_name:<15}")
            count += 1
        course_id = input_course_id()
        clear_screen()
        valid_course_id: str = ""
        course_name: str = ""
        try:
            for course in my_courses:
                if course_id.upper() == course.course_id.upper():
                    valid_course_id = course.course_id.upper()
                    course_name = course.course_name
                    break
            if valid_course_id == "":
                raise ValueError
        except ValueError:
            self.instructor_menu(error_message("CourseID not associated with any existing course."))

        my_students: [Student] = self._portal.get_student_enrolled_in(course_id=course_id)

        StringFormatting(f"Student offering {course_name} are: ").underline().bold().print()
        StringFormatting(f"{"s/n":>3} | {"Student-ID":>10} | {"Student Name":>15}").underline().bold().print()
        count = 1
        for student in my_students:
            StringFormatting(f"{count:>3} | {student.student_id:>10} | {student.full_name}").underline().print()
            count += 1
        input("press enter to continue...")
        self.instructor_menu("Welcome back to your menu!")

    def manage_account(self):
        ManageAccountMenu(self._instructor, self._portal).start()
        self.instructor_menu("Welcome back to your menu!")

