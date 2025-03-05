# from scms.course import Course
# from scms.grade import Grade
from scms.user import User, UserType

class Student(User):
    def __init__(self, student_id, full_name, email, password):
        super().__init__(
            student_id,
            full_name,
            email,
            password,
            UserType.STUDENT
        )
        # self.__enrolled_course:[Course] = []
        #
        # def enroll(course:Course) -> None:
        #     pass
        #
        # def drop(course:Course) -> None:
        #     pass
        #
        # def view_grades() -> [Grade]:
        #     pass

