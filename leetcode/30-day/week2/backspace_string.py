class Solution:
    
    def newStr(self,s:str) ->str:
        x = 0
        for i in range(0,len(s)):
            if s[i]=="#":
                if x>0:
                    x-=1
                    s = s[:-1]
            else:
                x+=1
                s+=(s[i])
        return s[(len(s)-x):]
    
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.newStr(S)==self.newStr(T)
        
        # not using O(1) space
        # newS  = ""
        # for c in S:
        #     if c=="#":
        #         newS = newS[:-1]
        #     else:
        #         newS+=c
        # newT  = ""
        # for c in T:
        #     if c=="#":
        #         newT = newT[:-1]
        #     else:
        #         newT+=c
        # return newS==newT