#include <iostream>
using namespace std;

int binarySearch(int ar[], int n, int key)
{
    int lb = 0, ub = n, mid;
    while (lb <= ub)
    {
        mid = (lb + ub) / 2;
        if (ar[mid] == key)
            return mid;
        if (ar[mid] > key)
            ub = mid - 1;
        else
            lb = mid + 1;
    }
    return -1;
}

// Test Code

int main()
{
    int ar[] = {1, 4, 6, 8, 10, 12}, n = 6;
    cout << "The position of 10 : " << binarySearch(ar, n, 10) + 1 << endl;
    return 0;
}