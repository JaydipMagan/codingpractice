"""
In a string S of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.

The final answer should be in lexicographic order.

Example 1:

Input: "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.

Example 2:

Input: "abc"
Output: []
Explanation: We have "a","b" and "c" but no large group.

Example 3:

Input: "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]

Note:  1 <= S.length <= 1000
"""
class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        n = len(S)
        matches = []
        i = 0
        while i<n:
            current_char = S[i]
            group_length = 1
            while group_length+i<n and current_char==S[group_length+i]:
                group_length+=1
            if group_length>=3:
                matches.append([i,i+group_length-1])
            i +=group_length
        return matches