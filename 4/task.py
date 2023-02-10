#1
a = int(input("введіть значення a: "))
b = int(input("введіть значення b: "))

sum = 0
for i in range(a, b+1):
    sum += i

print("Сума всіх натуральних чисел між a і b дорівнює:", sum)
#2
n = int(input("введіть число: "))

factorial = 1
for i in range(1, n+1):
    factorial *= i

print("Факторіал", n, "є", factorial)
#3
rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end = "")
    print()
#4
width = int(input("введіть ширину прямокутника: "))
height = int(input("введіть висоту прямокутника: "))
for i in range(height):
    for j in range(width):
        print("*", end="")
    print()
#5
width = int(input("введіть ширину прямокутника: "))
height = int(input("введіть висоту прямокутника: "))
for i in range(height):
    for j in range(width):
        print("*", end="")
    print()

#6
username = "admin"
password = "password"
attempts = 0
while attempts < 3:
    user_username = input("введіть username: ")
    user_password = input("введіть password: ")
    if user_username == username and user_password == password:
        print(f"Authentication успішна, passed on {attempts + 1} attempt.")
        break
    else:
        attempts += 1
        if attempts < 3:
            print("Incorrect login or password, please try again.")
        else:
            print("Maximum number of attempts reached.")