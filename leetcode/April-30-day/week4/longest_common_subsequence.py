"""
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:

    1 <= text1.length <= 1000
    1 <= text2.length <= 1000
    The input strings consist of lowercase English characters only.

"""
import collections

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    
        lcss = collections.defaultdict(lambda: -1)
        
        def lcs(x,y):
            if len(x)==0 or len(y)==0:
                return 0
            
            if x[-1:]==y[-1:]:
                key = (x,y)
                value = 1+lcs(x[:-1],y[:-1]) if lcss[key]==-1 else lcss[key]
                lcss[key]=value
                return value
            else:
                key, key1 = (x[:-1],y), (x,y[:-1])
                value = lcs(x[:-1],y) if lcss[key]==-1 else lcss[key]
                value1 = lcs(x,y[:-1]) if lcss[key1]==-1 else lcss[key1]
                lcss[key]=value
                lcss[key1]=value1
                return max(value,value1)
            
        return lcs(text1,text2)