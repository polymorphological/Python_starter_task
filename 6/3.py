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
