primes = []
numbers = list(range(2, 1001))

while numbers:
    prime = numbers[0]
    primes.append(prime)
    numbers = [n for n in numbers if n % prime != 0]

print(primes)
test