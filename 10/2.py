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
