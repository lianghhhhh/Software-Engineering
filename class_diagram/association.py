class Student:
    def __init__(self, name: str):
        self.name = name
        self.courses = []

    def enroll(self, course: 'Course'):
        self.courses.append(course)
        course.add_student(self)

    def print_courses(self):
        course_titles = [course.title for course in self.courses]
        print(f"{self.name} is enrolled in: {', '.join(course_titles)}")

class Course:
    def __init__(self, title: str):
        self.title = title
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def print_students(self):
        student_names = [student.name for student in self.students]
        print(f"Students enrolled in {self.title}: {', '.join(student_names)}")

if __name__ == "__main__":
    alice = Student("Alice")
    bob = Student("Bob")
    
    math = Course("Math")
    physics = Course("Physics")

    alice.enroll(math)
    alice.enroll(physics)
    bob.enroll(physics)

    alice.print_courses()
    bob.print_courses()
    math.print_students()
    physics.print_students()