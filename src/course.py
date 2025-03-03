class Course:
    def __init__(self, course_id, course_name, instructor):
        self.course_id = course_id
        self.course_name = course_name
        self.instructor = instructor
        self.students = []
        self.grades = {}

    def enroll_student(self, student):
        self.students.append(student)
        self.grades[student.user_id] = None

    def assign_grade(self, student, grade):
        self.grades[student.user_id] = grade