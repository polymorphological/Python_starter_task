#1
string = input('як тебе звати: ')
if string == 'Vadym':
    print('Привіт тьоска')
#2
import math

x = float(input("введіть значення "))
y = math.cos(3 * x)
print("y =", y)
#3
import math

a = float(input("введіть значення а: "))
b = float(input("введіть значення b: "))
c = float(input("введіть значення c: "))

#калькулятор дискримінанта
d = b**2 - 4*a*c


if d > 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print("значення: {} та {}".format(root1, root2))
elif d == 0:
    root1 = -b / (2*a)
    print("значення : {}".format(root1))
else:
    print("не дійсне рішення")
#4
import math

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")
print("6. Square root")
print("7. Cube root")
print("8. Sin")
print("9. Cos")
print("10. Tan")

# Take input from the user
choice = int(input("Enter choice(1/2/3/4/5/6/7/8/9/10): "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operations = {1: '+', 2: '-', 3: '*', 4: '/', 5: '^', 6: 'Square root', 7: 'Cube root', 8: 'Sin', 9: 'Cos', 10: 'Tan'}

if choice in range(1, 6):
    print(num1, operations[choice], num2, "=", eval(f"{num1} {operations[choice]} {num2}"))
elif choice in range(6, 11):
    if choice == 6:
        print(f"Square root of {num1} is {math.sqrt(num1)}")
    elif choice == 7:
        print(f"Cube root of {num1} is {num1 ** (1/3)}")
    else:
        print(f"{operations[choice]} of {num1} is {eval(f'math.{operations[choice]}({num1})')}")
else:
    print("Invalid input")
#5
num = int(input("Enter a number: "))

# Using ternary operator
print("The number is even." if num % 2 == 0 else "The number is odd.")
#6
day = input("Enter the day of the week: ").lower()

if day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday":
    print("Today is a work day.")
elif day == "saturday" or day == "sunday":
    print("Today is a weekend.")
else:
    print("This day does not exist.")

