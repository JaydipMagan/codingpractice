class Solution:
    def maxProfit(self, prices) -> int:
        max = 0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:#look back
                max += prices[i]-prices[i-1]
        return max
s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))