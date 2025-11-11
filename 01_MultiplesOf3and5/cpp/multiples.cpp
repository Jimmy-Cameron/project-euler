#include "multiples.hpp"

#include <iostream>
#include <optional>
#include <vector>

SumOfMultiples::SumOfMultiples(int val1, int val2, int limit)
    : mVal1 { val1 }
    , mVal2 { val2 }
    , mLimit { limit }
{
}

void SumOfMultiples::PrintInfo()
{
    std::cout << "Sum of multiples of " << mVal1 << " or " << mVal2 
        << " below " << mLimit << ":\n";
}

std::optional<int> SumOfMultiples::Calculate()
{
    std::vector<int> multiples {};
    for (int i = 0; i < mLimit; i++)
    {
        if (((i % mVal1) == 0)
            || ((i % mVal2) == 0))
        {
            multiples.push_back(i);
        }
    }

    int sum {};
    for (int num : multiples)
    {
        sum += num;
    }

    if (sum == 0)
    {
        return {};
    }
    else
    {
        return sum;
    }
}

