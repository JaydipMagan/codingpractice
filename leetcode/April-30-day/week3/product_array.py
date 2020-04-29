class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums)==2:
            nums.reverse()
            return nums
        
        result = [1]*len(nums)
        product = 1
        for i in range(0,len(result)-1):
            result[i+1] = product*nums[i]
            product = result[i+1]
        product = 1 * nums[-1]
        # print(result)
        for i in range(1,len(result)):
            i = len(result)-i-1
            temp = result[i]
            # print("temp",temp,"product",product)
            result[i] = result[i] * product
            # print(result[i])
            product = nums[i]*product
            # print(product)
        return result