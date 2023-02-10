int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []

for i in int_list:
    if i % 2 != 0:
        new_list.append(i)

repeat = int(input("Enter the number of times you want to repeat the new list: "))

for i in range(repeat):
    int_list += new_list

int_list.clear()
print(int_list)
