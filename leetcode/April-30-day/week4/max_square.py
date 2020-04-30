"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
                
        n = len(matrix)
        m = len(matrix[0]) if n>0 else 0
                    
        max_length = 0 
        dp = [[0]*(m+1) for i in range(0,n+1)]
        for y in range(1,n+1):
            for x in range(1,m+1):
                if matrix[y-1][x-1]=="1":
                    dp[y][x] = min(dp[y-1][x], dp[y][x-1], dp[y-1][x-1]) + 1
                    max_length = max(max_length,dp[y][x])
                
        return max_length**2