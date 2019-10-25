#include <iostream>
using namespace std;

void bubbleSort(int arr[], int n)
{
    int i, j, temp = 0;
    for (i = 0; i < n; i++)
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

    for (i = 0; i < n; i++)
    {
        cout << arr[i] << endl;
    }
}

// TEST CODE

int main()
{
    int i, n, array[100];
    cin >> n;
    for (i = 0; i < n; i++)
    {
        cin >> array[i];
    }
    bubbleSort(array, n);
    return 0;
}
