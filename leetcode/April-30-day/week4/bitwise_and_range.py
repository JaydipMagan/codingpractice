"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4

Example 2:

Input: [0,1]
Output: 0
"""
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # return m&n&(self.rangeBitwiseAnd(m>>1,n>>1)<<1) if n>m else n
        if m==n:
            return m
        if len(bin(m))!=len(bin(n)):
            return 0
        
        result = m
        
        for i in range(m + 1, n + 1):
            if i*2 <= n:
                return 0 
            result = result & i
            
        return result

