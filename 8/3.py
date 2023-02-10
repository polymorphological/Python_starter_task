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
