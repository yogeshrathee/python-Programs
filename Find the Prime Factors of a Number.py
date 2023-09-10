def prime_factors(n):
    factors = []
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n = n / divisor
        else:
            divisor += 1
    return factors

num = int(input("Enter a number: "))
factors = prime_factors(num)
print(f"The prime factors of {num} are: {factors}")
