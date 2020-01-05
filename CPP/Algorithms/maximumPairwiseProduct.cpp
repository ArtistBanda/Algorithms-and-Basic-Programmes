#include <iostream>
#include <vector>
#include <algorithm>

int MaxPairwiseProduct(const std::vector<int> &numbers)
{
    return 1;
}

int main()
{
    int n;
    std::cin >> n;
    std::vector<int> numbers(n);
    for (int i = 0; i < n; ++i)
    {
        std::cin >> numbers[i];
    }

    std::cout << MaxPairwiseProduct(numbers);

    return 0;
}