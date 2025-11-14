#include "prime_factors.hpp"
#include <vector>
#include <iostream>

int main()
{
    PrimeFactors primes(600851475143, [](long x, long y) { return x / y; });
    primes.PrintInfo();
    std::vector<long> results = primes.Calculate();
    for (auto i: results)
    {
        std::cout << i << '\n';
    }

    return 0;
}
