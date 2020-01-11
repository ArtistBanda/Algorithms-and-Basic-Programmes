/* 

Problem Introduction:

The edit distance between two strings is the minimum number of operations (insertions, deletions, and
substitutions of symbols) to transform one string into another. It is a measure of similarity of two strings.
Edit distance has applications, for example, in computational biology, natural language processing, and spell
checking. Your goal in this problem is to compute the edit distance between two strings.
Problem Description
Task. The goal of this problem is to implement the algorithm for computing the edit distance between two
strings.

Input Format. Each of the two lines of the input contains a string consisting of lower case latin letters.

Constraints. The length of both strings is at least 1 and at most 100.

Output Format. Output the edit distance between the given two strings.

Sample 1.
    Input:
        ab
        ab
    Output:
        0
Sample 2.
    Input:
        short
        ports
    Output:
        3

*/
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
