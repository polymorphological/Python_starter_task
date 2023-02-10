#1
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("мінімальне значення списку: ", min(list1))
print("максимальне значення списку: ", max(list1))
print("сума значень: ", sum(list1))
print("середнє значення списку: ", sum(list1)/len(list1))
#2
def unique_lists(list1, list2):
    unique_list = list(set(list1) - set(list2)) + list(set(list2) - set(list1))
    unique_list.sort()
    print("Unique values in order:", unique_list)
    unique_list.sort(reverse=True)
    print("Unique values in reverse order:", unique_list)

list1 = input("Enter values for list 1 separated by commas: ").split(",")
list2 = input("Enter values for list 2 separated by commas: ").split(",")
unique_lists(list1, list2)
#3
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

primes = []
for num in range(start, end+1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            primes.append(num)

print("Prime numbers in the range: ", primes)

choice = input("Do you want to see the sum or product of these prime numbers? (Type 'sum' or 'product')")
if choice == 'sum':
    print("Sum of prime numbers: ", sum(primes))
elif choice == 'product':
    product = 1
    for prime in primes:
        product *= prime
    print("Product of prime numbers: ", product)
else:
    print("Invalid choice.")
#4
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
#5
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
#6
int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = [i for i in int_list if i % 2 != 0]

value = int(input("Enter a value to find in new_list: "))
count = new_list.count(value)
position = new_list.index(value)

if count > 0:
    print(f"Value {value} found {count} times at position {position} in the new_list.")
else:
    print(f"Value {value} not found in the new_list.")
