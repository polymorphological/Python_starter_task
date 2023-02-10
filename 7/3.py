list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

unique_list1 = list(set(list1) - set(list2))
unique_list2 = list(set(list2) - set(list1))

print("Unique values in list1:", unique_list1)
print("Unique values in list2:", unique_list2)
