#pragma once

#include <optional>

class EvenFibonacci
{
public:
    EvenFibonacci(int limit);
    void PrintInfo();
    std::optional< int > Calculate();

private:
    int mLimit;
};
