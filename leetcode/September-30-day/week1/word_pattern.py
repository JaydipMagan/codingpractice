"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true

Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false

Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false

Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false

Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.
"""
class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        
        n = len(pattern)
        pattern_ = dict()
        string_ = dict()
        string = string.split(" ")
        
        if n!=len(string):
            return False

        for p, s in zip(pattern,string):
            if p not in pattern_:
                if s in string_:
                    return False
                else:
                    pattern_[p] = s
                    string_[s] = p
            elif pattern_[p]!=s:
                return False
            
        return True