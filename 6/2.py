def unique_lists(list1, list2):
    unique_list = list(set(list1) - set(list2)) + list(set(list2) - set(list1))
    unique_list.sort()
    print("Unique values in order:", unique_list)
    unique_list.sort(reverse=True)
    print("Unique values in reverse order:", unique_list)

list1 = input("Enter values for list 1 separated by commas: ").split(",")
list2 = input("Enter values for list 2 separated by commas: ").split(",")
unique_lists(list1, list2)
