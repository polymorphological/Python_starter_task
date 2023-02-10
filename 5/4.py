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

