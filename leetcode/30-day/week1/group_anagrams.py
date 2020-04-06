import itertools
from collections import Counter
class Solution:
    def is_anagram(self,str1, str2):
        # list_str1 = list(str1)
        # list_str1.sort()
        # list_str2 = list(str2)
        # list_str2.sort()

        # return (list_str1 == list_str2)
        if len(str1)!=len(str2):
            return False
        return Counter(str1) == Counter(str2)
    def groupAnagrams(self, strs):
        groups = []
        for word in strs:
            group = [x for x in strs if self.is_anagram(word,x)]
            groups.append(group)
        groups.sort()
        return list(k for k,_ in itertools.groupby(groups))
s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(s.groupAnagrams(["",""]))