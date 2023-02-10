def add_item(store_items):
    item_name = input("Enter the name of the item: ")
    item_price = float(input("Enter the price of the item: "))
    item_quantity = int(input("Enter the quantity of the item: "))
    item = (item_name, item_price, item_quantity)
    store_items.append(item)

store_items = []
while True:
    user_input = input("Would you like to add an item to the store? (yes/no) ")
    if user_input == "yes":
        add_item(store_items)
    elif user_input == "no":
        break
    else:
        print("Invalid input. Please try again.")

print("The items in the store are: ")
for item in store_items:
    print(f"{item[0]} with price ${item[1]} and quantity {item[2]}")