#include <iostream>

#include "fibonacci.hpp"

int main()
{
    EvenFibonacci evenFibonacci(4000000);
    evenFibonacci.PrintInfo();
    std::optional< int > result = evenFibonacci.Calculate();
    if (result)
    {
        std::cout << *result << '\n';
    }
    else 
    {
        std::cout << "Invalid limit";
    }
}
