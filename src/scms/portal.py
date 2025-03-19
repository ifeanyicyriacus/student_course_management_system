from src.scms.cryptography import Cryptography
from src.scms.course import Course
from src.scms.enrollment import Enrollment
from src.scms.student import Student
from src.scms.instructor import Instructor
from src.scms.data_restore import DataRestore
from src.scms.data_backup import DataBackup
from src.std_utility.io_function import error_message


class Portal:
    courses:[Course] = []
    enrollments:[Enrollment] = []
    students: [Student] = []
    instructors: [Instructor] = []

    def __init__(self):
        directory = "dev"
        data_restore = DataRestore(f"./../../data/{directory}/courses.txt",
                                   f"./../../data/{directory}/enrollments.txt",
                                   f"./../../data/{directory}/students.txt",
                                   f"./../../data/{directory}/instructors.txt")
        self.restored_data = data_restore.restore()

        data_backup = DataBackup(f"./../../data/{directory}/courses.txt",
                                   f"./../../data/{directory}/enrollments.txt",
                                   f"./../../data/{directory}/students.txt",
                                   f"./../../data/{directory}/instructors.txt")
        self.backup_course = data_backup.add_to_courses
        self.backup_enrollment = data_backup.add_to_enrollments
        self.backup_student = data_backup.add_to_students
        self.backup_instructor = data_backup.add_to_instructors
        self.override_student = data_backup.override_student_file
        self.override_instructor = data_backup.override_instructor_file


        self.courses: list[Course] = self.restored_data[0]
        self.enrollments: list[Enrollment] = self.restored_data[1]
        self.students:[Student] = self.restored_data[2]
        self.instructors:[Instructor] = self.restored_data[3]

        print(f"""
Data Restore Complete:
- {len(self.courses)} courses
- {len(self.enrollments)} enrollments
- {len(self.students)} students
- {len(self.instructors)} instructors
""")


    def register_instructor(self, full_name, email, password) -> None:
        new_buddy:Instructor = Instructor(self._generate_instructor_id(), full_name, email, password)
        self._add_user(new_buddy)

    def register_student(self, full_name, email, password) -> None:
        new_buddy:Student = Student(self._generate_student_id(), full_name, email, password)
        self._add_user(new_buddy)

    def check_duplicate_email(self, email:str) -> bool:
        for student in self.students:
            if student.email.lower() == email.lower():
                return True
        for instructor in self.instructors:
            if instructor.email.lower() == email.lower():
                return True
        return False

    def login(self, email:str, password:str) -> Student|Instructor|None:
        for student in self.students:
            if student.email == email and Cryptography.verify(password, student.password):
                return student

        for instructor in self.instructors:
            if instructor.email == email and Cryptography.verify(password, instructor.password):
                return instructor
        return None

    def _add_user(self, new_buddy:Student|Instructor) -> None:
        if type(new_buddy) is Student:
            self.students.append(new_buddy)
            self.backup_student(new_buddy)
        elif type(new_buddy) is Instructor:
            self.instructors.append(new_buddy)
            self.backup_instructor(new_buddy)

    def _generate_instructor_id(self) -> str:
        return f"INS{len(self.instructors) + 100000}"

    def _generate_student_id(self) -> str:
        return f"STU{len(self.instructors) + 100000}"

    def _generate_course_id(self) -> str:
        return f"COU{len(self.courses) + 1000}"

    def _course_exist(self, course_name:str) -> bool:
        for course in self.courses:
            if course.course_name == course_name:
                return True
        return False


    def add_course(self, course_name: str, course_description: str, instructor_id: str):
        new_course = Course(self._generate_course_id(), course_name, course_description, instructor_id)
        if self._course_exist(course_name):
            print(error_message(f"Course {new_course.course_name} already exists."))
        else:
            self.courses.append(new_course)
            self.backup_course(new_course)

    def add_enrollment(self, course_id:str, student_id:str):
        new_enrollment = Enrollment(course_id, student_id)
        if self._enrollment_exist(new_enrollment):
            print(error_message(f"Enrollment already exists."))
        else:
            self.enrollments.append(new_enrollment)
            self.backup_enrollment(new_enrollment)

    def _enrollment_exist(self, new_enrollment:Enrollment) -> bool:
        for enrollment in self.enrollments:
            if enrollment.course_id == new_enrollment.course_id and enrollment.student_id == new_enrollment.student_id:
                return True
        return False

    def get_courses_by(self, student_id:str) -> list[Course]:
        result:[Course] = []
        for enrollment in self.enrollments:
            if enrollment.student_id == student_id:
                for course in self.courses:
                    if course.course_id == enrollment.course_id:
                        result.append(course)
        return result

    def get_courses_and_grades_by(self, student_id:str) -> list:
        result:list = []
        for enrollment in self.enrollments:
            if enrollment.student_id == student_id:
                for course in self.courses:
                    if course.course_id == enrollment.course_id:
                        result.append({"course_name":course.course_name, "grade":enrollment.grade})
        return result

    def get_courses_and_instructors_by(self, student_id):
        my_courses_ids:[str] = self._get_my_courses_ids_by(student_id)
        my_courses:[Course] = self._get_my_courses_by(my_courses_ids)
        my_instructor_ids:[str] = _get_my_instructors_ids_by(my_courses)
        my_instructors:[Instructor] = self._get_my_instructors_by(my_instructor_ids)
        return my_courses, my_instructors

    def _get_my_courses_ids_by(self, student_id:str) -> [str]:
        # result:[str] = []
        # for enrollment in self.enrollments:
        #     if enrollment.student_id == student_id:
        #         result.append(enrollment.course_id)
        # return result
        return [enrollment.course_id for enrollment in self.enrollments if enrollment.student_id == student_id]

    def _get_my_courses_by(self, courses_ids:[str]) -> [Course]:
        # result:[Course] = []
        # for course in self.courses:
        #     if course.course_id in courses_ids:
        #         result.append(course)
        # return result
        return [course for course in self.courses if course.course_id in courses_ids]

    def _get_my_instructors_by(self, instructor_ids:[str]) -> [Instructor] :
        # result:[Instructor] = []
        # for instructor in self.instructors:
        #     if instructor.instructor_id in instructor_ids:
        #         result.append(instructor)
        # return result
        return [instructor for instructor in self.instructors if instructor.instructor_id in instructor_ids]

    def get_instructors_course_by(self, instructor_id:str) -> [Course]:
        return [course for course in self.courses if course.instructor_id == instructor_id]

    def override_student_file(self) -> None:
        self.override_student(self.students)

    def override_instructor_file(self) -> None:
        self.override_instructor(self.instructors)

def _get_my_instructors_ids_by(courses:[Course]) -> [str]:
    # result:[str] = []
    # for course in courses:
    #     result.append(course.instructor_id)
    # return result
    return [course.instructor_id for course in courses]