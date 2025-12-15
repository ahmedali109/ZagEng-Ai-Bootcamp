#Create variables to store your name, age, height, and whether you are a student. Print their types.

name = "Ahmed Ali Naguib"
age = 20
height = 190
college = "Faculty of Computer and Information Zagazig University"
# print variables types
print(type(name))
print(type(age))
print(type(height))
print(type(college))

#---------------------------------------------------------------------------------------------------------

# Ask the user for two numbers and print their sum, difference, product, and division.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Division:", num1 / num2)

#---------------------------------------------------------------------------------------------------------

# Take an intger input and check if it’s positive, negative, or zero
number = int(input("Enter an number: "))
if number > 0:
    print("The Number is Positive")
elif number < 0:
    print("The Number is Negative")
else:
    print("The Number is Zero")

#---------------------------------------------------------------------------------------------------------

# Print all even numbers between 1 and 20.
even = [num for num in range(1, 21) if num % 2 == 0]
print("Even numbers between 1 and 20:", even)

#---------------------------------------------------------------------------------------------------------

# Ask the user to guess a number (secret = 7) until they get it right.
secretNumber = 7
failed = 0
try:
    while True:
        guess = int(input("Guess the secret number: "))
        if guess == secretNumber:
            print("Congratulations! You guessed it right.")
            break
        if failed >= 2:
            print("The secret number is", secretNumber)
            print("Better luck next time!")
            break
        else:
            failed += 1
            print("Try again.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
    
#---------------------------------------------------------------------------------------------------------

# Create a text file named data.txt, write a few lines, then read and print its content.
with open("data.txt", "w") as file:
    file.write("Hello, this is a sample text file.\n")
    file.write("It contains multiple lines of text.\n")
    file.write("This is the third line.\n")

with open("data.txt", "r") as file:
    content = file.read()
    print("Content of data.txt:")
    print(content)

#---------------------------------------------------------------------------------------------------------

# Create a list of 5 numbers, print the sum, maximum, and reverse it.
numbers = [10, 25, 5, 40, 15]

sum = 0
for num in numbers:
    sum += num
print("Sum:", sum)
print("Maximum:", max(numbers))
print("Reversed List:", numbers[::-1])

#---------------------------------------------------------------------------------------------------------

# Create a tuple of city names, and print the first and last city.

cities = ("Cairo", "Alexandria", "Giza", "Luxor", "Aswan")
print("First City:" , cities[0])
print("Last City:" , cities[-1])

#---------------------------------------------------------------------------------------------------------

# Given two sets of student names, find those who are in both groups.
groupA = {"Ahmed", "Sara", "Mona", "Omar"}
groupB = {"Mona", "Ali", "Sara", "Hassan"}
common_students = groupA.intersection(groupB)
print("Students in both groups:", common_students)

#---------------------------------------------------------------------------------------------------------

# Handle division by zero using try and except.

try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    result = numerator / denominator
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")

#---------------------------------------------------------------------------------------------------------

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def average_temperature(temp_list, scale):
    if scale == 'C' or scale == 'c':
        total = sum(temp_list)
        return total / len(temp_list)
    elif scale == 'F' or scale == 'f':
        total = sum(temp_list)
        return total / len(temp_list)
    else:
        return None

def highest_temperature(temp_list, scale):
    if scale == 'C' or scale == 'c':
        return max(temp_list)
    elif scale == 'F' or scale == 'f':
        return max(temp_list)
    else:
        return None

temp_input = input("Enter a list of temperatures in Celsius (comma-separated): ")
temp_celsius = [float(temp) for temp in temp_input.split(",")]
avg_celsius = average_temperature(temp_celsius, 'C')
highest_celsius = highest_temperature(temp_celsius, 'C')
print(f"Average Temperature in Celsius: {avg_celsius:.2f}°C")
print(f"Highest Temperature in Celsius: {highest_celsius:.2f}°C")