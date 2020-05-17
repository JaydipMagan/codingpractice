"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""
import collections
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        groups = collections.defaultdict(list)
        for i in range(0,n-m+1):
            sub = s[i:i+m]
            key = "".join(sorted(sub))
            groups[key].append(i)
        key = "".join(sorted(p))
        return groups[key]

"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = "".join(sorted(p))
        l = len(p)
        ls = len(s)
        indicies = []

        i = l -1
        pre = False
        while i < ls:
            if pre and s[i] == s[i-l]:
                indicies.append(i-l+1)
                i += 1
            elif s[i] in p:
                if p == "".join(sorted(s[i-l+1:i+1])):
                    indicies.append(i-l+1)
                    pre = True
                else:
                    pre = False
                i += 1
            else:
                i += l
                pre = False
        return indicies
"""