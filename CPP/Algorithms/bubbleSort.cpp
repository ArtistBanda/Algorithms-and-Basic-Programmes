#include <iostream>
using namespace std;

void bubbleSort(int arr[], int n)
{
    int i, j, temp = 0;
    for (i = 0; i < n - 1; i++)
    {
        for (j = 0; j < n - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                temp = arr[j + 1];
                arr[j + 1] = arr[j];
                arr[j] = temp;
            }
        }
    }
}

// Test Code

int main()
{
    int i, n, ar[100];
    cin >> n;
    for (i = 0; i < n; i++)
    {
        cin >> ar[i];
    }
    bubbleSort(ar, n);
    for (int i = 0; i < n; i++)
        cout << ar[i] << ' ';
    return 0;
}
