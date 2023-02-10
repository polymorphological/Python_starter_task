print("Введіть цифру")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
discr = (b ** 2 - 4 * a * c)**2
print("Дискримінант D = %.2f" % discr)
if discr > 0:
    x1 = (-b + (discr)) / (2 * a)
    x2 = (-b - (discr)) / (2 * a) 
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
elif discr < 0:
    print(complex(discr))


