import operator

def FindNthPrime(input):
    n = input
    prime = [True for i in range(n + 1)]
    p = 2 # we know this as first prime

    while(p*p <= n):
        if prime[p] == True:
            # mark all multiples of p as false (non prime)
            # we use n+1 to cover the case where input is a prime
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    # create a list of all found primes
    primes = []
    for i in range(2, n + 1):
        if prime[i]:
            primes.append(i)

    return primes
    # return max(primes, default = 0)

# main loop
if __name__=='__main__':
    primes = FindNthPrime(int(input("Input: ")))

    try:
        if primes[10001-1]:
            print(f"Prime Value: {primes[10001-1]}")
    except:
        print(f"Nope.")
