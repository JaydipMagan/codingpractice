"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""
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