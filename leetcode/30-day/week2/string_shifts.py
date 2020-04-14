class Solution:
    def stringShift(self, s, shift) -> str:
            if len(s)==1: 
                return s
            
            for row in shift:
                shift_amount = row[1]
                if row[0]==0: # shift left
                    s = s[shift_amount:]+s[:shift_amount]
                else:
                    s = s[len(s)-shift_amount:]+s[:len(s)-shift_amount]
            return s

s = Solution()

s.stringShift("abcdefg",[[1,1],[1,1],[0,2],[1,3]])