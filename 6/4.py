list = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    list.append(int(input("Enter element: ")))

while True:
    choice = int(input("Enter 1 to print list in reverse order or 2 to print in ascending order or any other key to exit: "))
    if choice == 1:
        print(list[::-1])
    elif choice == 2:
        list.sort()
        print(list)
    else:
        break
