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