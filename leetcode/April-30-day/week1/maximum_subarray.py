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