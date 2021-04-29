"""
Given a string A, partition A such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of A.



Input Format:

The first and the only argument contains the string A.
Output Format:

Return an integer, representing the answer as described in the problem statement.
Constraints:

1 <= length(A) <= 501
Examples:

Input 1:
    A = "aba"

Output 1:
    0

Explanation 1:
    "aba" is already a palindrome, so no cuts are needed.

Input 2:
    A = "aab"
    
Output 2:
    1

Explanation 2:
    Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""

def isPalindrome(x):
	return x == x[::-1]


def minPalPartion(string, i, j):
	if i >= j or isPalindrome(string[i:j + 1]):
		return 0
	ans = float('inf')
	for k in range(i, j):
		count = (
			1 + minPalPartion(string, i, k)
			+ minPalPartion(string, k + 1, j)
		)
		ans = min(ans, count)
	return ans


def main():
	string = "aab"
	print(minPalPartion(string, 0, len(string) - 1))

if __name__ == "__main__":
	main()
