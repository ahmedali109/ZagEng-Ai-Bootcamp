def get_valid_int(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter an integer between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_student_info():
    name = input("Enter student's name: ")
    age = get_valid_int("Enter student's age (5-100): ", 5, 100)
    grade = get_valid_int("Enter student's grade (0-100): ", 0, 100)
    return {"name": name, "age": age, "grade": grade}

def calculate_averages(students):
    total_age = sum(student['age'] for student in students)
    total_grade = sum(student['grade'] for student in students)
    count = len(students)
    avg_age = total_age / count if count > 0 else 0
    avg_grade = total_grade / count if count > 0 else 0
    return avg_age, avg_grade

def save_to_file(filesName , studentData):
    with open(filesName , "w") as file:
        file.write(studentData)

def read_from_file(fileName):
    with open(fileName , "r") as file:
        content = file.read()
    return content

def main():
    students = {}
    while True:
        print("1. Add Student \n2. View Students \n3. Calculate Averages \n4. Save to File \n5. Read from File \n6. Exit")
        choice = input("Choose an option (1-6): ")
        if choice == '1':
            student = get_student_info()
            if student['name'] in students:
                print("Student already exists...")
                continue
            students[student['name']] = student
        elif choice == '2':
            for student in students.values():
                print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
        elif choice == '3':
            avg_age, avg_grade = calculate_averages(students.values())
            print(f"Average Age: {avg_age:.2f}, Average Grade: {avg_grade:.2f}")
        elif choice == '4':
            studentData = "\n".join([f"Name: {s['name']}, Age: {s['age']}, Grade: {s['grade']}" for s in students.values()])
            save_to_file("students.txt", studentData)
            print("Data saved to students.txt")
        elif choice == '5':
            content = read_from_file("students.txt")
            print("Content of students.txt:" , content)
        elif choice == '6':
            exit()
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()