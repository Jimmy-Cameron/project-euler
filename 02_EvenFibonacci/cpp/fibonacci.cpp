#include "fibonacci.hpp"

#include <iostream>

EvenFibonacci::EvenFibonacci(int limit)
    : mLimit { limit }
{
}

void EvenFibonacci::PrintInfo()
{
    std::cout << "Sum of even Fibonacci numbers below " << mLimit << '\n';
}

std::optional< int > EvenFibonacci::Calculate()
{
    if (this->mLimit <= 0)
    {
        return {};
    }
    else 
    {
        int val1 { 1 };
        int val2 { 2 };
        int sum { 2 };
        int nextVal { 0 };

        while (nextVal < this->mLimit)
        {
            nextVal = val1 + val2;
            sum += ((nextVal % 2) == 0) ? nextVal : 0; 

            val1 = val2;
            val2 = nextVal;
        }

        return sum;
    }
}
