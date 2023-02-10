int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = [i for i in int_list if i % 2 != 0]

value = int(input("Enter a value to find in new_list: "))
count = new_list.count(value)
position = new_list.index(value)

if count > 0:
    print(f"Value {value} found {count} times at position {position} in the new_list.")
else:
    print(f"Value {value} not found in the new_list.")
