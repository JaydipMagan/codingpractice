class Solution:
    def hammingWeight(self, n: int) -> int:

        s = bin(n)[2:]
        
        return len([bit for bit in s if bit=="1"])