class Solution:
    
    
    def checkValidString(self, s: str) -> bool:

        if s=="":
            return True
        
        n = len(s)
        left,right = 0,0 # keep count of left and right brackets
        for i in range(0,n):
            x = s[i] # left side
            y = s[n-i-1] # right side
            if x =="*" or x=="(":
                left+=1
            else:
                left-=1
                
            if y=="*" or y==")":
                right+=1
            else:
                right-=1
                
            if right<0 or left<0:
                return False
            
        return True
            