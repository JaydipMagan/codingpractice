"""
 Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

    Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    Any right parenthesis ')' must have a corresponding left parenthesis '('.
    Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
    An empty string is also valid.

Example 1:

Input: "()"
Output: True

Example 2:

Input: "(*)"
Output: True

Example 3:

Input: "(*))"
Output: True

Note:

    The string size will be in the range [1, 100].
"""
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
            