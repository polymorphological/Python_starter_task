import math

def quadratic_equation(a, b, c):
    x1, x2 = None, None
    
    def calc_result():
        nonlocal x1, x2
        D = b**2 - 4 * a * c
        if D >= 0:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
        else:
            x1 = None
            x2 = None
    
    calc_result()
    return x1, x2

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

roots = quadratic_equation(a, b, c)
print("Roots: ", roots)
