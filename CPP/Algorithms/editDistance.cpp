#include <iostream>
#include <string>
#include <algorithm>

using std::min;
using std::string;

int edit_distance(const string &str1, const string &str2)
{
    int n = str1.size(), m = str2.size();
    int distance[n + 1][m + 1] = {0};
    int ins, del, mm;
    for (int i = 0; i <= n; i++)
        distance[i][0] = i;
    for (int i = 0; i <= m; i++)
        distance[0][i] = i;
    for (int i = 1; i <= m; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            ins = distance[j][i - 1] + 1;
            del = distance[j - 1][i] + 1;
            if (str1[j - 1] != str2[i - 1])
                mm = distance[j - 1][i - 1] + 1;
            else
                mm = distance[j - 1][i - 1];
            distance[j][i] = min(ins, min(del, mm));
        }
    }

    return distance[n][m];
}

int main()
{
    string str1;
    string str2;
    std::cin >> str1 >> str2;
    std::cout << edit_distance(str1, str2) << std::endl;
    return 0;
}
