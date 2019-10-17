#include <iostream>
using namespace std;
void insertionSort(int ar[], int start, int end)
{
    if (start >= end)
        return;
    else
    {
        int curPos, temp;
        curPos = temp = 0;
        for (int i = start + 1; i < end; i++)
        {
            curPos = i;
            while (curPos > 0 && (ar[curPos] < ar[curPos - 1]))
            {
                temp = ar[curPos];
                ar[curPos] = ar[curPos - 1];
                ar[curPos - 1] = temp;

                curPos -= 1;
            }
        }
    }
}

// Test Code

int main()
{
    int n;
    cin >> n;
    int ar[n];
    for (int i = 0; i < n; i++)
        cin >> ar[i];
    insertionSort(ar, 0, n);
    for (int i = 0; i < n; i++)
        cout << ar[i] << ' ';
    cout << endl;
    return 0;
}