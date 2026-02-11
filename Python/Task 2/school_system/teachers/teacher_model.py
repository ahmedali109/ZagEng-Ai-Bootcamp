class Teacher:
    def __init__(self , id , name , specialty):
        self.id = id
        self.name = name
        self.specialty = specialty
    def show_details(self):
        return f"Teacher ID: {self.id}, Name: {self.name}, Specialty: {self.specialty}"