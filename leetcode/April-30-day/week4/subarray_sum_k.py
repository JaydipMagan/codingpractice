"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2

Note:

    The length of the array is in range [1, 20,000].
    The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""
import collections
class Solution:
    def optimised(self, nums: List[int], k: int) -> int:
        subarrays = 0
        n = len(nums)
        sum_freq  = collections.defaultdict(int)
        temp_sum = 0
        sum_freq[0] = 1 # make dictionary with 0 and 1 so no if statements needed later
        
        
        for num in nums:
            temp_sum+=num # sum so far
            subarrays+= sum_freq[temp_sum-k] # check if difference in hashmap then add to counter
            sum_freq[temp_sum]+= 1 #update freq for sum so far
            

        return subarrays

    def subarraySum(self, nums: List[int], k: int) -> int:
        
        subarrays = 0
        n = len(nums)
        sum_freq  = collections.defaultdict(int)
        temp_sum = 0
        for num in nums:
            
            temp_sum+=num # sum so far
            if temp_sum==k:
                subarrays+=1
            
            # check if difference in hashmap
            if temp_sum-k in sum_freq.keys():
                subarrays += sum_freq[temp_sum-k]
            
            sum_freq[temp_sum]+=1
            
            

        return subarrays