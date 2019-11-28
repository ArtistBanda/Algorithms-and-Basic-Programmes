#include <iostream>
#include <stdlib.h>
using namespace std;

void selectionSort(int ar[], int n)
{
    int min_index, temp;
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = i + 1; j < n; j++)
            if (ar[min_index] > ar[j])
                min_index = j;

        temp = ar[min_index];
        ar[min_index] = ar[i];
        ar[i] = temp;
    }
}

// Test Code

int main()
{
    int ar[] = {1, 6, 5, 2, 0, 10, 3, 12};
    int n = sizeof(ar) / sizeof(ar[0]);
    selectionSort(ar, n);
    for (int i = 0; i < n; i++)
        cout << ar[i] << ' ';
    return 0;
}