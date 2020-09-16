"""
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
"""
class Solution:
    def findMaximumXOR(self, nums):
        ans, mask = 0, 0
        for i in range(31, -1, -1):
            mask |= 1<<i
            found = set([num & mask for num in nums])
                
            start = ans | 1<<i
            for pref in found:
                if start^pref in found:
                    ans = start
                    break
         
        return ans