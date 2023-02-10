name = input("введіть ФІО: ")
if name.isalpha():
    name = name.title()
    print("Ваше імя: ", name)
else:
    print("невірно введено.")