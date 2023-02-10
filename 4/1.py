a = int(input("введіть значення a: "))
b = int(input("введіть значення b: "))

sum = 0
for i in range(a, b+1):
    sum += i

print("Сума всіх натуральних чисел між a і b дорівнює:", sum)