"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_ = bin(x)[2:]
        y_ = bin(y)[2:]
        
        if len(x_)>=len(y_):
            y_ = y_.zfill(len(x_))
        else:
            x_ = x_.zfill(len(y_))
        
        # print(x_,y_)
        z = list(filter(lambda m : m==True,map(lambda m, n: m!=n,x_,y_)))
        # print(z)
        return len(z)

        import math
        def hammingDistanceEff(self, x: int, y: int) -> int:
            if x==y:
                return 0
            else:
                z = x^y
                z = bin(z)
                return z.count('1')