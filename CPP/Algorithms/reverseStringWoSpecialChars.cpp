#include <iostream>
#include <ctype.h>
#include <string.h>

using namespace std;

void reverseStringWoSpecialChars(char *str)
{
    int startPtr = 0;
    int endPtr = strlen(str) - 1;

    while (startPtr < endPtr)
    {
        if (!isalpha(str[startPtr]))
            startPtr++;
        else if (!isalpha(str[endPtr]))
            endPtr--;
        else
        {
            swap(str[startPtr], str[endPtr]);
            startPtr++;
            endPtr;
        }
    }
}

// Test Code

int main()
{
    char str[] = "a!!!b.c.d,e'f,ghi";
    cout << "Original String : " << str << endl;
    reverseStringWoSpecialChars(str);
    cout << "Reversed without affecting special chars : " << str << endl;
    return 0;
}