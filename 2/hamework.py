#1
a = int(input('Введіть перше число:'))
b = int(input('Введіть друге число:'))
c = int(input('Введіть третє число:'))
result = None
result = a * b * c
print(result)
#2
a = int(input('Введіть перше число:'))
b = int(input('Введіть друге число:'))
c = int(input('Введіть друге число:'))
print(a*b*c)
#3
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
#4
phrase = input("введіть фразу з 10 символів: ")
if len(phrase) != 10:
    print("помилка фраза не є з 10 символів")
else:
    ascii_sum = 0
    for char in phrase:
        ascii_sum += ord(char)
    print(ascii_sum)
#5
def reversed1(variable):
    res=[]
    for i in range(len(variable)-1,-1,-1):
        res.append(variable[i])
    res=''.join(res)
    return res

n = reversed1(input())
print(n)
#6
radius = int(input("Введіть радіус круга : "))

print("Площа = ", 3.14 * radius **2)
#7
length = 700
x = length
velocity = 90
y = velocity
driving_time = x / y

print("driving_time : ", driving_time)
#8
A = str(input("Як вас звати ? :"))
B = str(input("Скільки вам років ? :"))
print("My name is" , A , "and I am" , B )