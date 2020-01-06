#include <iostream>
#include <vector>
#include <algorithm>

int MaxPairwiseProduct(const std::vector<int> &numbers)
{
    int n = numbers.size(), max_index1, max_index2;
    max_index1 = 0;

    for (int i = 1; i < n; i++)
        if (numbers[i] > numbers[max_index1])
            max_index1 = i;

    if (max_index1 == 0)
        max_index2 = 1;
    else
        max_index2 = 0;

    for (int i = 1; i < n; i++)
        if (numbers[i] > numbers[max_index2] && i != max_index1)
            max_index2 = i;

    return numbers[max_index1] * numbers[max_index2];
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