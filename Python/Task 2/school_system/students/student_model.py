class Student:
    def __init__(self , id , name , courses):
        self.id = id
        self.name = name
        self.courses = courses
    def enroll(self , course):
        self.courses.append(course)
    def show_details(self):
        course_titles = ', '.join([course.title for course in self.courses])
        return f"Student ID: {self.id}, Name: {self.name}, Courses: {course_titles}"