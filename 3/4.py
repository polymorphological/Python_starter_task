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
