"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:

int isMatch(const char *s, const char *p)
Some examples:

isMatch("aa","a") → 0
isMatch("aa","aa") → 1
isMatch("aaa","aa") → 0
isMatch("aa", "a*") → 1
isMatch("aa", ".*") → 1
isMatch("ab", ".*") → 1
isMatch("aab", "c*a*b") → 1
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""


def strrmatch(strr, pattern, n, m):

    # empty pattern can only match with
    # empty strring
    if m == 0:
        return n == 0

    # lookup table for storing results of
    # subproblems
    lookup = [[False for i in range(m + 1)] for j in range(n + 1)]

    # empty pattern can match with empty strring
    lookup[0][0] = True

    # Only '*' can match with empty strring
    for j in range(1, m + 1):
        if pattern[j - 1] == "*":
            lookup[0][j] = lookup[0][j - 1]

    # fill the table in bottom-up fashion
    for i in range(1, n + 1):
        for j in range(1, m + 1):

            # Two cases if we see a '*'
            # a) We ignore ‘*’ character and move
            # to next character in the pattern,
            # i.e., ‘*’ indicates an empty sequence.
            # b) '*' character matches with ith
            # character in input
            if pattern[j - 1] == "*":
                lookup[i][j] = lookup[i][j - 1] or lookup[i - 1][j]

            # Current characters are considered as
            # matching in two cases
            # (a) current character of pattern is '.'
            # (b) characters actually match
            elif pattern[j - 1] == "." or strr[i - 1] == pattern[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1]

            # If characters don't match
            else:
                lookup[i][j] = False

    return lookup[n][m]


# Driver code


strr = "aa"
pattern = ".*"

if strrmatch(strr, pattern, len(strr), len(pattern)):
    print(1)
else:
    print(0)
