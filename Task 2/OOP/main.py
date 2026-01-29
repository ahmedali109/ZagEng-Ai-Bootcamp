class USER:
    def __init__(self , name , email , __password):
        self.name = name
        self.email = email
        self.__password = __password
    def show_info(self):
        return f"Name: {self.name}, Email: {self.email}"

class Student(USER):
    StudentMap = {
        "Beginner": "Has basic understanding of programming concepts.",
        "Intermediate": "Comfortable with programming and can build small projects.",
        "Advanced": "Proficient in programming and can handle complex projects."
    }
    def __init__(self, name, email, __password , level):
        super().__init__(name, email, __password)
        self.level = level
        self._Student__password = __password
    def setPassword(self , new_password):
        self.__password = new_password
    def check_password(self , password):
        return self._Student__password == password
    def show_info(self):
        return super().show_info() + f", Level: {self.level}"
   
class Instructor(USER):
    def __init__(self, name, email, __password , expertise):
        super().__init__(name, email, __password)
        self.expertise = expertise
        self._Instructor__password = __password
    def setPassword(self , new_password):
        self.__password = new_password
    def check_password(self , password):
        return self._Instructor__password == password
    def show_info(self):
        return super().show_info() + f", Expertise: {self.expertise}"
        
# Example Usage
student = Student("John Doe", "john@example.com", "password123", "Beginner")
instructor = Instructor("Jane Smith", "jane@example.com", "securepass", "Mathematics")

print(student.show_info())
print(Student.StudentMap[student.level])
print(instructor.show_info())
print(f"Instructor Expertise: {instructor.expertise}")
print(student.check_password("password123"))
print(instructor.check_password("wrongpass"))
print(student.show_info())
print(instructor.show_info())