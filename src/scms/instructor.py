class Instructor:
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)
        self.courses_taught = []

    def create_course(self, course):
        self.courses_taught.append(course)
        print(f"Course {course.course_name} created.")

    def view_students(self, course):
        for student in course.students:
            print(student.name)
