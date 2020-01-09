#include <iostream>
#include <string>
#include <algorithm>

using std::min;
using std::string;

int edit_distance(const string &str1, const string &str2)
{
}

int main()
{
    string str1;
    string str2;
    std::cin >> str1 >> str2;
    std::cout << edit_distance(str1, str2) << std::endl;
    return 0;
}
