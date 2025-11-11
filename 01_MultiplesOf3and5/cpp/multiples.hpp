#pragma once

#include <optional>

class SumOfMultiples
{
public:
    SumOfMultiples(int val1, int val2, int limit);
    void PrintInfo();
    std::optional<int> Calculate();

private:
    int mVal1{};
    int mVal2{};
    int mLimit{};
};
