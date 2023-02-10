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
