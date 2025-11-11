#include "multiples.hpp"

#include <iostream>

int main()
{
    SumOfMultiples answer{ 3, 5, 1000 };

    answer.PrintInfo();
    std::optional<int> result = answer.Calculate();

    if (result)
    {
        std::cout << *result << '\n';
    }
    else
    {
        std::cout << "No multiples found.\n";
    }

    return 0;
}
