def prime_factors(input):
    factors = []
    div = 2
    while input > 1:
        while input % div == 0:
            factors.append(div)
            input /= div
        div += 1
    return factors

# main loop
factors = prime_factors(600851475143)
print(max(factors)) # print the largest prime factor from the list
