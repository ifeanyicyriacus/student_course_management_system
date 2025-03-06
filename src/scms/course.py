from scms.enrollment import Enrollment

# from scms.instructor import Instructor
# from scms.student import Student


class Course:
    def __init__(self, course_id:str, course_name:str, course_description:str, instructor_assigned):
        self.course_id = course_id
        self.course_name = course_name
        self.course_description = course_description
        self.instructor_assigned = instructor_assigned
        self.enrolled_student:list = []

    @property
    def course_id(self):
        return self.__course_id
    @course_id.setter
    def course_id(self, value):
        self.__course_id = value

    @property
    def course_name(self):
        return self.__course_id
    @course_name.setter
    def course_name(self, value):
        self._course_name = value

    @property
    def course_description(self):
        return self.__course_description
    @course_description.setter
    def course_description(self, value):
        self.__course_description = value

    @property
    def instructor_assigned(self):
        return self.__instructor_assigned
    @instructor_assigned.setter
    def instructor_assigned(self, value):
        self.__instructor_assigned = value


    def add_student(self, student):
        pass

    def remove_student(self, student):
            pass