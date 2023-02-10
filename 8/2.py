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
