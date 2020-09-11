"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0: 
            return 0 
        if len(nums) == 1: 
            return nums[0]
            
        min_,max_,out= nums[0], nums[0], nums[0]
        
        for i in range(1,len(nums)):
            max__ = max(nums[i],max_*nums[i],min_*nums[i])            
            min__ = min(nums[i],max_*nums[i],min_*nums[i])
            max_,min_ = max__, min__
            out = max(max_,out)
        
        return out