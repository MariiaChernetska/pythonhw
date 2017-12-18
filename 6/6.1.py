
def prime_gen(start, end):
    while start <= end:
        isPrime = True
        for x in range(2, start):
            if start % x == 0:
                isPrime = False
                break

        if isPrime:
            yield start

        start += 1


print(list(prime_gen(5, 100)))
