"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        size = 2**n
        powerset = [[]]
        for i in range(1,size):
            binary = bin(i)[2:].zfill(n)
            subset = [nums[j] for j in range(0,n) if binary[j]=="1"]
            powerset.append(subset)
            
        return powerset
    
    
    
    def subsetsEff(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        
        return output