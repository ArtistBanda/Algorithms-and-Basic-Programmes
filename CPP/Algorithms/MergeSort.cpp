#include <iostream>
#include <stdlib.h>
using namespace std;

void merge(int ar[], int left, int right, int mid)
{
    int n1, n2;
    n1 = mid - left + 1;
    n2 = right - mid;

    int temp1[n1], temp2[n2];

    for (int i = 0; i < n1; i++)
        temp1[i] = ar[left + i];
    for (int i = 0; i < n2; i++)
        temp2[i] = ar[mid + i + 1];

    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2)
    {
        if (temp1[i] < temp2[j])
            ar[k++] = temp1[i++];
        else
            ar[k++] = temp2[j++];
    }

    while (i < n1)
        ar[k++] = temp1[i++];
    while (j < n2)
        ar[k++] = temp2[j++];
}

void mergeSort(int ar[], int left, int right)
{
    if (left < right)
    {
        int mid = left + (right - left) / 2;
        mergeSort(ar, left, mid);
        mergeSort(ar, mid + 1, right);
        merge(ar, left, right, mid);
    }
}

// Test Code

int main()
{
    int ar[] = {1, 5, 2, 3, 0, 9};
    int n = sizeof(ar) / sizeof(ar[0]);
    mergeSort(ar, 0, n - 1);
    for (int i = 0; i < n; i++)
        cout << ar[i] << ' ';
    return 0;
}