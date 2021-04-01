"""
Given an array of non-negative integers, A, of length N, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Return the minimum number of jumps required to reach the last index.

If it is not possible to reach the last index, return -1.

Input Format:

The first and the only argument contains an integer array, A.
Output Format:

Return an integer, representing the answer as described in the problem statement.
Constraints:

1 <= N <= 1e6
0 <= A[i] <= 50000
Examples:

Input 1:
    A = [2, 1, 1]

Output 1:
    1
    
Explanation 1:
    The shortest way to reach index 2 is
        Index 0 -> Index 2
    that requires only 1 jump.

Input 2:
    A = [2,3,1,1,4]

Output 2:
    2

Explanation 2:
    The shortest way to reach index 4 is
        Index 0 -> Index 1 -> Index 4
    that requires 2 jumps.
"""

class Solution:
    def jump(self, arr):
        n = len(arr)
        jumps = [0 for i in range(n)]
     
        if n == 1:
            return arr[0]
        if (n == 0) or (arr[0] == 0):
            return -1
     
        jumps[0] = 0
     
        # Find the minimum number of
        # jumps to reach arr[i] from
        # arr[0] and assign this
        # value to jumps[i]
        for i in range(1, n):
            jumps[i] = float('inf')
            for j in range(i):
                if (i <= j + arr[j]) and (jumps[j] != float('inf')):
                    jumps[i] = min(jumps[i], jumps[j] + 1)
                    break
        return jumps[n-1]


Solver = Solution()
print(Solver.jump([2,3,1,1,4]))
