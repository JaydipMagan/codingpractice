"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:

    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.

"""
class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        amount_nonzero = 0 
        for i in range(0, len(nums)):
            if (nums[i] !=0): 
                nums[amount_nonzero], nums[i] = nums[i], nums[amount_nonzero] #swap
                amount_nonzero+=1
        # print(nums)
s = Solution()
s.moveZeroes([0,1,0,3,12])