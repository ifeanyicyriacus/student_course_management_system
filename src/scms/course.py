from scms.enrollment import Enrollment

# from scms.instructor import Instructor
# from scms.student import Student


class Course:
    def __init__(self, course_id: str, course_name: str, course_description: str, instructor_id: str):
        self.course_id = course_id
        self.course_name = course_name
        self.course_description = course_description
        self.instructor_id = instructor_id

    @property
    def course_id(self):
        return self.__course_id

    @course_id.setter
    def course_id(self, value: str):
        if not value:
            raise ValueError("Course ID cannot be empty.")
        self.__course_id = value

    @property
    def course_name(self):
        return self.__course_name

    @course_name.setter
    def course_name(self, value: str):
        if not value:
            raise ValueError("Course name cannot be empty.")
        self.__course_name = value

    @property
    def course_description(self):
        return self.__course_description

    @course_description.setter
    def course_description(self, value: str):
        if not value:
            raise ValueError("Course description cannot be empty.")
        self.__course_description = value

    @property
    def instructor_id(self):
        return self.__instructor_id

    @instructor_id.setter
    def instructor_id(self, value: str):
        if not value:
            raise ValueError("Instructor ID cannot be empty.")
        self.__instructor_id = value


