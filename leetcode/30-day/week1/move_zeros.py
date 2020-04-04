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