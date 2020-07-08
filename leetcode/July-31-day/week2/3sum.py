"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        freq = collections.Counter(nums)
        nums = sorted(freq)
        
        res = []
        
        for k ,v in enumerate(nums):
            if v==0:
                if freq[v]>2:
                    res.append([0,0,0])
            elif freq[v]>1 and -2*v in freq:
                res.append([v,v,-2*v])
            

            if v<0:
                opp = -v
                left = bisect_left(nums, opp - nums[-1], k + 1)
                right = bisect_right(nums, opp / 2, left)
                
                for a in nums[left:right]:
                    b = opp -a
                    if b in freq and a!=b:
                        res.append([v,a,b])
        return res