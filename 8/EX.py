#1
def greet_user(name=None):
    if name:
        print("Hello, " + name + "!")
    else:
        print("Hello, user! What's your name?")
#2
import math

def sin_expression(x):
    return x * math.sin(x)

def cos_expression(x):
    return x * math.cos(x)

print("x\tsin_expression(x)\tcos_expression(x)")

x = -5
while x <= 5:
    sin_value = sin_expression(x)
    cos_value = cos_expression(x)
    print("%.1f\t%.2f\t\t\t%.2f" % (x, sin_value, cos_value))
    x += 0.5
#3
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    return a ** 0.5

def cube_root(a):
    return a ** (1/3)

while True:
    print("Enter 1 for addition")
    print("Enter 2 for subtraction")
    print("Enter 3 for multiplication")
    print("Enter 4 for division")
    print("Enter 5 for power")
    print("Enter 6 for square root")
    print("Enter 7 for cube root")
    print("Enter anything else to quit")
    user_choice = int(input("Enter your choice: "))

    if user_choice in [1, 2, 3, 4, 5]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if user_choice == 1:
            result = addition(a, b)
        elif user_choice == 2:
            result = subtraction(a, b)
        elif user_choice == 3:
            result = multiplication(a, b)
        elif user_choice == 4:
            result = division(a, b)
        elif user_choice == 5:
            result = power(a, b)
        print("Result:", result)
    elif user_choice in [6, 7]:
        a = float(input("Enter number: "))
        if user_choice == 6:
            result = square_root(a)
        elif user_choice == 7:
            result = cube_root(a)
        print("Result:", result)
    else:
        break
#4
def average_of_three_numbers(a, b, c):
    return (a + b + c) / 3

while True:
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        c = float(input("Enter the third number: "))
        result = average_of_three_numbers(a, b, c)
        print("The average of the three numbers is:", result)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    break
#5
def bmi_calculator(height, weight):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        return "Normal weight"
    else:
        return "Overweight"

while True:
    height = input("Enter your height (m): ")
    if height == "off":
        break
    height = float(height)

    weight = input("Enter your weight (kg): ")
    if weight == "off":
        break
    weight = float(weight)

    result = bmi_calculator(height, weight)
    print("Your body mass index is: ", result)
