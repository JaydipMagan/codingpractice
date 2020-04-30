"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1

Example 2:

Input: [4,1,2,1,2]
Output: 4
"""


class Solution:
    def singleNumber(self, nums) -> int:
        seen = dict([ (p,0) for p in nums ])
        to_return = nums[0]
        for x in nums:
            if seen[x]==0:
                to_return = x
            elif seen[x]==1:
                seen[x] = seen[x]+1
        return to_return

s = Solution()
a = s.singleNumber([4,1,2,1,2])
print(a)