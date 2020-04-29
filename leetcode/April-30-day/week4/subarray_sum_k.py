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