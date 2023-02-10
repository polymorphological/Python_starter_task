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
