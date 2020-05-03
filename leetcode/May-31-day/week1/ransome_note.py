"""
 Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

"""

import collections
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = collections.Counter(magazine)
        construct = True
        for char in ransomNote:
            if freq[char]>0:
                freq[char]-=1
                construct&=True
            else:
                construct&=False
        return construct
    