"""
Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

Example 1:

Input: [1,2,3,4]
Output: "23:41"

Example 2:

Input: [5,5,5,5]
Output: ""

Note:

    A.length == 4
    0 <= A[i] <= 9
"""
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        # a b : c d 
        
        max_time = -1
        
        for a,b,c,d in itertools.permutations(A):
            # HH<24 and MM < 60
            h = ((a*10)+b)
            m = ((c*10)+d)
            if h<24 and m<60:
                t = h*60 + m
                max_time = max(max_time,t)
                
        return "" if max_time==-1 else "{:02d}:{:02d}".format(max_time // 60, max_time % 60)