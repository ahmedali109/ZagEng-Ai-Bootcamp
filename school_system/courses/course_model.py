class Course:
    def __init__(self , id , title , teacher):
        self.id = id
        self.title = title
        self.teacher = teacher
    def show_details(self):
        return f"Course ID: {self.id}, Title: {self.title}, Teacher: {self.teacher}"