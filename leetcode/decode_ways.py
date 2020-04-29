
class Solution:
    
    def numDecodings(self, s: str) -> int:
        def split(str, num):
            return [ str[start:start+num] for start in range(0, len(str), num) ]
        def rec(s):
            if len(s)%2==0: # even
                pass
        # 0 -> 0
        # 1 -> 1
        # 12 -> 2
        # 123 -> 3
        # 129 -> 2
        # 120 -> 1
        # 101 -> 1
        # 10 -> 2
        # 100 -> 0
        # 1000 -> 0
        # 1100 - > 
        
        # 123123 = 1
        # 1 23 12 3 -> 1 2 3 12 3 -> 1 23 1 2 3 = 3 
        # 12 31 23 -> 1 2 31 23 -> 12 3 1 23 -> 12 31 2 3 -> 1 2 3 1 23 -> 12 3 1 2 3 -> 12 3 1 2 3 = 5 ignore >26
        
        # 1231234
        # 1 23 12 34
        # 12 31 23 4
        if s=="0":
            return 0
        if len(s)%2!=1:
        print(s[0],split(s[1:],2))
        print(split(s[:-1],2),s[-1])
        return 1

s = Solution()
# print(s.numDecodings("123"))
print(s.numDecodings("123123"))