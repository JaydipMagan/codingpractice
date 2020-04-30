"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:

Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:

Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000. 
"""
class Solution:
    
    def findMaxLength(self, nums: List[int]) -> int:
        #max size of nums = 50,000
        counter,counter_vals,max_value = 0,{0:0},0
        for index,value in enumerate(nums):
            counter += 2*value -1 # if value is 0 then counter will be -1 else 1. Equal 1s AND 0s mean counter = 0 at the end
            if counter in counter_vals: # check if counter was in dict already
                max_value = max(max_value,index+1-counter_vals[counter])
            else:
                counter_vals[counter] = index+1                
        return max_value 