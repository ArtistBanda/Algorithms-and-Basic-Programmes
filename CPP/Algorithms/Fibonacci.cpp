#include <iostream>

using namespace std;

long long fibonacci_naive(int value)
{
    if (value <= 1)
        return value;
    else
        return fibonacci_naive(value - 1) + fibonacci_naive(value - 2);
}

int main()
{
    int n;
    cin >> n;
    cout << fibonacci_naive(n);
}