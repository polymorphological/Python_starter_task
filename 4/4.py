width = int(input("введіть ширину прямокутника: "))
height = int(input("введіть висоту прямокутника: "))
for i in range(height):
    for j in range(width):
        print("*", end="")
    print()
