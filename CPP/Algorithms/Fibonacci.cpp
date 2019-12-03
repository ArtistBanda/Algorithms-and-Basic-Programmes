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
    // pass parameter arr of size value + 1 initilized with zeros

    if (arr[value])
        return arr[value];

    if (value <= 1)
        return value;

    else
        arr[value] = fibonacci_euclid(value - 1, arr) + fibonacci_euclid(value - 2, arr);

    return arr[value];
}

long long fibonacci_euclid_iterative(int value)
{
    long long arr[value + 1];

    arr[0] = 0;
    arr[1] = 1;

    for (int i = 2; i <= value; i++)
        arr[i] = arr[i - 1] + arr[i - 2];

    return arr[value];
}

// Test Code

int main()
{
    int n;
    cin >> n;
    long long arr[n + 1];
    cout << fibonacci_euclid(n, arr);
}