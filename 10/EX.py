#2
import math
import random

from math import pi
from math import e

repeats = int(input('Enter the number of repeats: '))
print_ = 5
print(print_ * repeats)
print(pi * print_ * repeats)
print(e * 2)

while print_ >= 0:
    print_ -= 1

string = 'my string'
result = 0
for elem in string:
    result += pow(string.find(elem), 2)
print("result=", result)

def my_func(attribute=1):
    print('attribute', attribute)

print(my_func(attribute=5))
#3
import math

def menu():
    print("1. Корень квадратний")
    print("2. Експонента")
    print("3. Логарифм")
    print("4. Тригонометрична функція")
    print("5. Вихід")
    return int(input("Виберіть пункт меню: "))

def main():
    while True:
        choice = menu()
        if choice == 1:
            number = float(input("Введіть число: "))
            result = math.sqrt(number)
            print("Корінь квадратний з %.2f = %.2f" % (number, result))
        elif choice == 2:
            number = float(input("Введіть число: "))
            result = math.exp(number)
            print("e в степені %.2f = %.2f" % (number, result))
        elif choice == 3:
            number = float(input("Введіть число: "))
            result = math.log(number)
            print("Натуральний логарифм з %.2f = %.2f" % (number, result))
        elif choice == 4:
            number = float(input("Введіть число: "))
            print("1. Синус")
            print("2. Косинус")
            print("3. Тангенс")
            func = int(input("Виберіть тригонометричну функцію: "))
            if func == 1:
                result = math.sin(number)
                print("Синус з %.2f = %.2f" % (number, result))
            elif func == 2:
                result = math.cos(number)
                print("Косинус з %.2f = %.2f" % (number, result))
            elif func == 3:
                result = math.tan(number)
                print("Тангенс з %.2f = %.2f" % (number, result))
        elif choice == 5:
            break

if __name__ == "__main__":
    main()
#4
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