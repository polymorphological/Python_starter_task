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
