"""
Given two sequences A, B, count number of unique ways in sequence A, to form a subsequence that is identical to the sequence B.

Subsequence : A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, “ACE” is a subsequence of “ABCDE” while “AEC” is not).

Input Format:

The first argument of input contains a string, A.
The second argument of input contains a string, B.
Output Format:

Return an integer representing the answer as described in the problem statement.
Constraints:

1 <= length(A), length(B) <= 700
Example :

Input 1:
    A = "abc"
    B = "abc"
    
Output 1:
    1

Explanation 1:
    Both the strings are equal.

Input 2:
    A = "rabbbit" 
    B = "rabbit"

Output 2:
    3

Explanation 2:
    These are the possible removals of characters:
        => A = "ra_bbit" 
        => A = "rab_bit" 
        => A = "rabb_it"
        
    Note: "_" marks the removed character.
"""


def numDistinct(S, T):
    m = len(T)
    n = len(S)

    # T can't appear as a subsequence in S
    if m > n:
        return 0

    # mat[i][j] stores the count of
    # occurrences of T(1..i) in S(1..j).
    mat = [[0 for _ in range(n + 1)] for __ in range(m + 1)]

    # Initializing first column with all 0s. x
    # An empty string can't have another
    # string as suhsequence
    for i in range(1, m + 1):
        mat[i][0] = 0

    # Initializing first row with all 1s.
    # An empty string is subsequence of all.
    for j in range(n + 1):
        mat[0][j] = 1

    # Fill mat[][] in bottom up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            # If last characters don't match,
            # then value is same as the value
            # without last character in S.
            if T[i - 1] != S[j - 1]:
                mat[i][j] = mat[i][j - 1]

            # Else value is obtained considering two cases.
            # a) All substrings without last character in S
            # b) All substrings without last characters in
            # both.
            else:
                mat[i][j] = mat[i][j - 1] + mat[i - 1][j - 1]

    return mat[m][n]


print(numDistinct("rabbbit", "rabbit"))