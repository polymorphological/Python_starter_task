numbers = input("введіть послідовність чисел,розділених пробілами: ")
numbers_tuple = tuple(map(int, numbers.split()))
sorted_tuple = sorted(numbers_tuple)
print(sorted_tuple)