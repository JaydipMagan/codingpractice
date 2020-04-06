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