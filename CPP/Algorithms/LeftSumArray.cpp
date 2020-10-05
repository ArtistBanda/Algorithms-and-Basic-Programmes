// Given, an array of size n. Find an element that divides the array into two sub-arrays with equal sum.

#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int naive_method(vector<int> list, int n)
{
    // Slower method
    // O(n^2)
    vector<int>::iterator it;
    int counter = 0;
    for (it = list.begin(); it != list.end(); it++)
    {
        int sum1 = accumulate(list.begin(), it, 0);
        int sum2 = accumulate(it + 1, list.end(), 0);

        if (sum1 == sum2)
            counter++;
    }
    return counter;
}

int fast_method(vector<int> list, int n)
{
    // Faster method
    // O(n)

    vector<int> left_sum, right_sum;
    vector<int>::iterator it, it2;

    int counter = 0, temp_sum = 0;

    for (it = list.begin(); it != list.end(); it++)
    {
        temp_sum += *it;
        left_sum.push_back(temp_sum);
    }
    temp_sum = 0;

    for (it = list.end() - 1; it != list.begin() - 1; it--)
    {
        temp_sum += *it;
        right_sum.push_back(temp_sum);
    }

    for (it = left_sum.begin(), it2 = right_sum.begin(); it != left_sum.end(); it++, it2++)
    {
        if (*it == *it2)
            counter++;
    }

    return counter;
}

int main()
{
    // Test Code

    int n = 6;
    vector<int> vect{2, 3, 4, 1, 5, 4};
    cout << fast_method(vect, n);
}