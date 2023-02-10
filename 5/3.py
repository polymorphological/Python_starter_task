def RGB_to_color(red, green, blue):
    return (red, green, blue)

r = int(input("введіть значення червоного: "))
g = int(input("введіть значення зеленого: "))
b = int(input("введіть значення синього: "))

color = RGB_to_color(r, g, b)
print(color)