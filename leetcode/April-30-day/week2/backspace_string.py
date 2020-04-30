"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

Note:

    1 <= S.length <= 200
    1 <= T.length <= 200
    S and T only contain lowercase letters and '#' characters.

Follow up:

    Can you solve it in O(N) time and O(1) space?

"""
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