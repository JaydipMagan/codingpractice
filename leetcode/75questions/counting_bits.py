class Solution:
    def countBits(self, n: int):
        
        
        dp = [0]
        
        power = 1
        counter = power 

        for i in range(0,n):
            print("counter",counter)
            x = i+1

            print(x)
            if power*2==x:
                power = x
                counter = power
                
            offset = power - counter
            counter-=1
            res = 1 + dp[offset]       
            dp.append(res)
        
        print("dp",dp)

s = Solution()
s.countBits(16)