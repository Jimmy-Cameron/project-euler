#include <iostream>
#include <vector>

#include "prime_factors.hpp"

PrimeFactors::PrimeFactors(long limit, std::function< long ( long, long ) > op)
    : mLimit { limit }
    , operation(op)
{
}

PrimeFactors::~PrimeFactors() = default;

void PrimeFactors::PrintInfo()
{
    std::cout << "Largest prime factor below " << mLimit << '\n';
}

std::vector< long > PrimeFactors::Calculate()
{
    long currVal = mLimit;
    long div = 2;
    std::vector< long > primes {};

    while (currVal > 1)
    {
        while (currVal % div == 0)
        {
            primes.push_back(div);
            currVal = operation(currVal, div);
        }

        div += 1;
    }

    return primes;
}
