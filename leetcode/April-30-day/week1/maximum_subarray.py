"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

class Solution:
    
    def maxSubArray(self, nums) -> int:
        if len(nums) == 0: 
            return 0 
        if len(nums) == 1: 
            return nums[0]
            
        output_sum = nums[0]
        current_sum = nums[0]
        for i in range(1,len(nums)):
            current_sum = max(current_sum+nums[i],nums[i])
            output_sum = max(current_sum,output_sum)
                             
        return output_sum