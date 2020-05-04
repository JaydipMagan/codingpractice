"""
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Example 1:

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

Example 2:

Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.

Note:

    The given integer is guaranteed to fit within the range of a 32-bit signed integer.
    You could assume no leading zero bit in the integer’s binary representation.
"""
class Solution:
    def findComplement(self, num: int) -> int:
            binRep = str(bin(num))[2:]
            comp = ""
            for digit in binRep:
                # comp += "0" if digit=="1" else "1" # slow for some reason
                comp += str(1-int(digit))
            return int(comp,2)
        
    def alt(self,num):
        if num == 0: return 1
        t = num
        res = 0
        while t > 0:
            t = t >> 1
            res = res << 1
            res += 1
        return res ^ num