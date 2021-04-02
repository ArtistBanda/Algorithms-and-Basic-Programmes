"""
Find the contiguous subarray within an array, A of length N which has the largest sum.

Input Format:

The first and the only argument contains an integer array, A.
Output Format:

Return an integer representing the maximum possible sum of the contiguous subarray.
Constraints:

1 <= N <= 1e6
-1000 <= A[i] <= 1000
For example:

Input 1:
    A = [1, 2, 3, 4, -10]

Output 1:
    10

Explanation 1:
    The subarray [1, 2, 3, 4] has the maximum possible sum of 10.

Input 2:
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Output 2:
    6

Explanation 2:
    The subarray [4,-1,2,1] has the maximum possible sum of 6.
"""
class Solution:
    def maxSubArray(self, a):
        size = len(a)
        
        max_so_far = -1000 - 1
        max_ending_here = 0
          
        for i in range(0, size):
            max_ending_here = max_ending_here + a[i]
            if (max_so_far < max_ending_here):
                max_so_far = max_ending_here
     
            if max_ending_here < 0:
                max_ending_here = 0  
        return max_so_far
        
solver = Solution()
print(solver.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    
