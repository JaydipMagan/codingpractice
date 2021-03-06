"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

"""
class Solution:
    def search(self, nums, target) -> int:
        def binSearch(l,h):
            if h>=l:
                m = l + (h - l) //2
                #normal bin search
                if nums[m]==t:
                    return m
                elif (nums[l]<=t<nums[m] or nums[m]<nums[h]) and (nums[l]<=t<nums[m] or not(nums[m]<t<=nums[h])):
                    return binSearch(l,m-1)
                else:
                    return binSearch(m+1,h)
            else:
                return -1
        t = target
        x = binSearch(0,len(nums)-1)
        return x
s = Solution()
# s.search([4,5,6,7,0,1,2],10)
s.search([4,5,6,7,8,1,2,3],8)
