phrase = input("введіть фразу з 10 символів: ")
if len(phrase) != 10:
    print("помилка фраза не є з 10 символів")
else:
    ascii_sum = 0
    for char in phrase:
        ascii_sum += ord(char)
    print(ascii_sum)