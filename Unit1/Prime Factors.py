n = int(input("Enter a number: "))

primes = []

num = n/2

if num % 2 != 0:
    num = n/3
    if num % 3 != 0:
        num = n/5

else:
    primes.append(num)

print(primes)
