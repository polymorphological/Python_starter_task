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
