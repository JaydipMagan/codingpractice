"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        common = freq.most_common()
        res = 0
        for i in range(len(common)):
            a,b = common[i][0], common[i][1]
            fit = b//2 # how many times 2 goes into b
            rem = b%2 # remainder when b divided by 2
            if fit>0:
                res+=(fit*2)
                freq[a] = b-(fit*2)
        for a,b in freq.most_common():
            if b>0:
                res+=1
                break
        
        return res
        