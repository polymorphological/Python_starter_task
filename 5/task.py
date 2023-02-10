#1
name = input("введіть ФІО: ")
if name.isalpha():
    name = name.title()
    print("Ваше імя: ", name)
else:
    print("невірно введено.")
#2
numbers = []

print("введіть діапазон чисел (не менше 5):")

while len(numbers) < 5:
    number = int(input())
    numbers.append(number)

second = numbers[1]
second_to_last = numbers[-2]
average = sum(numbers) / len(numbers)
result = second + second_to_last + average

print("сума другого передостаннього і середнього рівна:", result)
#3
def RGB_to_color(red, green, blue):
    return (red, green, blue)

r = int(input("введіть значення червоного: "))
g = int(input("введіть значення зеленого: "))
b = int(input("введіть значення синього: "))

color = RGB_to_color(r, g, b)
print(color)
#4
from collections import namedtuple

# створення фабрики іменованих кортежів
StudentScore = namedtuple('StudentScore', ['algebra', 'geometry', 'history', 'informatics', 'geography'])

# створення екземплярів кортежів
student1 = StudentScore(4, 5, 3, 5, 4)
student2 = StudentScore(4, 4, 5, 4, 4)
student3 = StudentScore(4, 3, 4, 4, 3)

# вивід даних на екран
print(student1)
print(student2)
print(student3)
#5
numbers = input("введіть послідовність чисел,розділених пробілами: ")
numbers_tuple = tuple(map(int, numbers.split()))
sorted_tuple = sorted(numbers_tuple)
print(sorted_tuple)
#6
feedback = input("будь ласка залишне свій відгук для 'Морська Зірка': ")

discount = 0

if "menu" in feedback.lower():
    discount += 5
if "gym" in feedback.lower() or "sportzal" in feedback.lower():
    discount += 5
if "service" in feedback.lower() or "obsluzhuvannya" in feedback.lower():
    discount += 5

if len(feedback) > 60:
    discount += 15

print("ваша знижка наступного разу складає : " + str(discount) + "%")