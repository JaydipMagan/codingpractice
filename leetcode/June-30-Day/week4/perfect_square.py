"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""
class Solution:
    def numSquares(self, n: int) -> int:
        
        dp = [inf for _ in range(n+1)]
        dp[0] = 0
        for i in range(1,n+1):
            j = 1
            while j*j<=i:
                x = j*j
                dp[i] = min(dp[i],1+dp[i-x])
                j+=1
        return dp[n]

    # More efficient
    def numSquares(self, n: int) -> int:
        while( n % 4 == 0 ):	# Reduction by factor of 4
            n /= 4
			
        if n % 8 == 7:			# If n = 8k + 7, returns 4
            return 4
			
        for a in range( int(sqrt(n))+1 ):	# Check if n = a^2 + b^2, return 0 / 1
            b = int(sqrt(n - a**2))
            if a**2 + b**2 == n:
                return (a>0) + (b>0)
				
        return 3				# If n = a^2 + b^2 + c^2, return 3
