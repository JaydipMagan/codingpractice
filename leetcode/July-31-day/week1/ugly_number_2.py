"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note:  

    1 is typically treated as an ugly number.
    n does not exceed 1690.
"""
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n<0: return 0
        
        ugly_nums = [1]
        index_2 = 0
        index_3 = 0 
        index_5 = 0

        while len(ugly_nums)<n:
            mult_2 = ugly_nums[index_2]*2
            mult_3 = ugly_nums[index_3]*3
            mult_5 = ugly_nums[index_5]*5
            min_ = min(mult_2,mult_3,mult_5)
            ugly_nums.append(min_)
            
            if min_==mult_2: index_2+=1
            if min_==mult_3: index_3+=1
            if min_==mult_5: index_5+=1
        return ugly_nums[-1]