from scms.cryptography import Cryptography
from src.scms.course import Course
from src.scms.enrollment import Enrollment
from scms.student import Student
from scms.instructor import Instructor
from src.scms.data_restore import DataRestore
from src.scms.data_backup import DataBackup



class Portal:
    course:[Course] = []
    enrollment:[Enrollment] = []
    users: [Student | Instructor] = []


    def __init__(self):
        directory = "dev"
        data_restore = DataRestore(f"./../../data/{directory}/courses.txt",
                                   f"./../../data/{directory}/enrollments.txt",
                                   f"./../../data/{directory}/students.txt",
                                   f"./../../data/{directory}/instructors.txt")
        self.restored_data = data_restore.restore()

        data_backup = DataBackup(f"./../../data/{directory}/courses.txt",
                                   f"./../../data/{directory}/enrollments.txt",
                                   f"./../data/{directory}/students.txt",
                                   f"./../../data/{directory}/instructors.txt")
        self.backup_course = data_backup.add_to_courses
        self.backup_enrollment = data_backup.add_to_enrollments
        self.backup_student = data_backup.add_to_students
        self.backup_instructor = data_backup.add_to_instructors

        self.courses: list[Course] = self.restored_data[0]
        self.enrollments: list[Enrollment] = self.restored_data[1]
        self.users:[Student|Instructor] = self.restored_data[2] + self.restored_data[3]


    def register_instructor(self, full_name, email, password) -> None:
        new_buddy:Instructor = Instructor("", full_name, email, password)
        self.add_user(new_buddy)

    def register_student(self, full_name, email, password) -> None:
        new_buddy:Student = Student("", full_name, email, password)
        self.add_user(new_buddy)

    def check_duplicate_email(self, email:str) -> bool:
        for user in self.users:
            if user.email.lower() == email.lower():
                return True
        return False


    def login(self, email, password) -> Student|Instructor|None:
        for user in self.users:
            if user.email == email and Cryptography.verify(password, user.password):
                return user
        return None

    def add_user(self, new_buddy:Student|Instructor) -> None:
        self.users.append(new_buddy)
        if new_buddy is Student:
            self.backup_student(new_buddy)
        elif new_buddy is Instructor:
            self.backup_instructor(new_buddy)

    # def find_user_by_email(self, email):
    #     for user in self.users:
    #         if user.email == email:
    #             return user
