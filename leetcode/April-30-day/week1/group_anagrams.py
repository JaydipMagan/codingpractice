"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:

    All inputs will be in lowercase.
    The order of your output does not matter.

"""
import collections
class Solution:
    def groupAnagrams(self, strs):
        groups = collections.defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            groups[key].append(word)

        return groups.values()
        
s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(s.groupAnagrams(["",""]))