#2
def is_palindrome(phrase):
    phrase = phrase.lower().replace(" ", "")
    return phrase == phrase[::-1]

input_phrase = input("Enter a phrase: ")
if is_palindrome(input_phrase):
    print("The phrase is a palindrome")
else:
    print("The phrase is not a palindrome")
#3
def ways_to_climb(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return ways_to_climb(n - 1) + ways_to_climb(n - 2)
#4
def sum_of_natural_numbers(start, end):
    if start > end:
        return 0
    return start + sum_of_natural_numbers(start + 1, end)

print(sum_of_natural_numbers(1, 10))
#5
import math

def quadratic_equation(a, b, c):
    x1, x2 = None, None
    
    def calc_result():
        nonlocal x1, x2
        D = b**2 - 4 * a * c
        if D >= 0:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
        else:
            x1 = None
            x2 = None
    
    calc_result()
    return x1, x2

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

roots = quadratic_equation(a, b, c)
print("Roots: ", roots)