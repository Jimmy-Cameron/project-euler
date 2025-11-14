#include <functional>
#include <vector>

class PrimeFactors
{
public:
    PrimeFactors(long limit, std::function< long ( long, long ) > op);
    ~PrimeFactors();
    void PrintInfo();
    std::vector< long > Calculate();

private:
    long mLimit = 0;
    std::function< long ( long, long ) > operation;
};
