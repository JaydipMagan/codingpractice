class Solution:
    def isHappy(self, n) -> bool:
        
        sum = 0
        computed = {}
        while n!=1:
            for d in map(int,str(n)):
                sum += d*d
            if computed.get(sum)==None:
                computed[sum] = sum
            else:
                return False
            print(sum)
            n = sum
            sum = 0
        return True


s = Solution()
A = s.isHappy(2)
print(A)