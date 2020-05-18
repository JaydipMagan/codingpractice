"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False

Note:

    The input strings only contain lower case letters.
    The length of both given strings is in range [1, 10,000].

"""
class Solution:
    def checkInclusion(self, p: str, s: str) -> bool:
        p = "".join(sorted(p))
        l = len(p)
        n = len(s)
        indicies = []

        i = l -1
        pre = False
        while i < n:
            if pre and s[i] == s[i-l]:
                return True
            elif s[i] in p:
                if p == "".join(sorted(s[i-l+1:i+1])):
                    return True
                else:
                    pre = False
                i += 1
            else:
                i += l
                pre = False
        return False