from scms.cryptography import Cryptography
from src.scms.course import Course
from src.scms.enrollment import Enrollment
from scms.student import Student
from scms.instructor import Instructor
from src.scms.data_restore import DataRestore
from src.scms.data_backup import DataBackup


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

        self.courses: list[Course] = self.restored_data[0]
        self.enrollments: list[Enrollment] = self.restored_data[1]
        self.students:[Student] = self.restored_data[2]
        self.instructors:[Instructor] = self.restored_data[3]


    def register_instructor(self, full_name, email, password) -> None:
        new_buddy:Instructor = Instructor(self.generate_instructor_id(), full_name, email, password)
        self.add_user(new_buddy)

    def register_student(self, full_name, email, password) -> None:
        new_buddy:Student = Student(self.generate_student_id(), full_name, email, password)
        self.add_user(new_buddy)

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

    def add_user(self, new_buddy:Student|Instructor) -> None:
        if type(new_buddy) is Student:
            self.students.append(new_buddy)
            self.backup_student(new_buddy)
        elif type(new_buddy) is Instructor:
            self.instructors.append(new_buddy)
            self.backup_instructor(new_buddy)


    def generate_instructor_id(self) -> str:
        return f"INS{len(self.instructors) + 100000}"

    def generate_student_id(self) -> str:
        return f"STU{len(self.instructors) + 100000}"

    def generate_course_id(self) -> str:
        return f"COU{len(self.courses) + 100000}"
