from src.scms.course import Course
from src.scms.enrollment import Enrollment
from src.scms.instructor import Instructor
from src.scms.student import Student
from src.scms.file_handler import FileHandler


class DataLoader:
    def __init__(self, courses_file_path:str, enrollments_file_path:str, students_file_path:str, instructors_file_path:str):
        self.__courses_file_handler: FileHandler = FileHandler(courses_file_path)
        self.__enrollments_file_handler: FileHandler = FileHandler(enrollments_file_path)
        self.__students_file_handler: FileHandler = FileHandler(students_file_path)
        self.__instructors_file_handler: FileHandler = FileHandler(instructors_file_path)

    def get_courses(self) -> list[Course]:
        courses:[Course] = []
        for course_info in self.__courses_file_handler.read():
            course_attributes:[str] = course_info.split(",")
            courses.append(Course(course_id=course_attributes[0].strip(),
                                  course_name=course_attributes[1].strip(),
                                  course_description=course_attributes[2].strip(),
                                  instructor_id=course_attributes[3].strip()))
        return courses

    def get_enrollments(self) -> list[Enrollment]:
        enrollments:[Enrollment] = []
        for enrollment_info in self.__enrollments_file_handler.read():
            enrollment_attributes:[str] = enrollment_info.split(",")
            enrollments.append(Enrollment(course_id=enrollment_attributes[0].strip(),
                                          student_id=enrollment_attributes[1].strip(),
                                          grade=enrollment_attributes[2].strip(),
                                          timestamp=enrollment_attributes[3].strip()))
        return enrollments

    def get_students(self) -> list[Student]:
        students:[Student] = []
        for student_info in self.__students_file_handler.read():
            student_attributes:[str] = student_info.split(",")
            students.append(Student(student_id=student_attributes[0].strip(),
                                    full_name=student_attributes[1].strip(),
                                    email=student_attributes[2].strip(),
                                    password=student_attributes[3].strip()))
        return students

    def get_instructors(self) -> list[Instructor]:
        instructors:[Instructor] = []
        for instructor_info in self.__instructors_file_handler.read():
            instructor_attributes:[str] = instructor_info.split(",")
            instructors.append(Instructor(instructor_id=instructor_attributes[0].strip(),
                                          full_name=instructor_attributes[1].strip(),
                                          email=instructor_attributes[2].strip(),
                                          password=instructor_attributes[3].strip()))
        return instructors
