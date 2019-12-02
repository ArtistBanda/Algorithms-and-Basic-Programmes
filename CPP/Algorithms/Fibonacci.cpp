#include <iostream>

using namespace std;

long long fibonacci_naive(int value)
{
    if (value <= 1)
        return value;
    else
        return fibonacci_naive(value - 1) + fibonacci_naive(value - 2);
}

long long fibonacci_euclid(int value, long long arr[])
{
    if (arr[value])
        return arr[value];

    if (value <= 1)
        return value;

    else
        arr[value] = fibonacci_euclid(value - 1, arr) + fibonacci_euclid(value - 2, arr);

    return arr[value];
}

int main()
{
    int n;
    cin >> n;
    long long arr[n + 1];
    cout << fibonacci_euclid(n, arr);
}