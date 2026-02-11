from courses.course_model import Course
from students.student_model import Student
from teachers.teacher_model import Teacher

def main():
    # Example usage
    teacher = Teacher(id=1, name="Mr. Smith", specialty="Mathematics")
    course = Course(id=101, title="Algebra", teacher=teacher)
    student = Student(id=1001, name="Alice", courses=[course])
    student.enroll(Course(id=102, title="Geometry", teacher=teacher))
    print(student.show_details())
    
if __name__ == "__main__":
    main()