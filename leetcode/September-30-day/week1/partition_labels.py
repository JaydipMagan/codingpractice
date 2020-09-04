"""
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:

    S will have length in range [1, 500].
    S will consist of lowercase English letters ('a' to 'z') only.
"""
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        ind = {c: i for i, c in enumerate(S)}        
        curr, res = 0, [0]
        
        while curr < len(S):
            
            last = ind[S[curr]]
            
            while curr <= last:
                symbol = S[curr]
                last = max(last, ind[symbol])
                curr += 1
            res.append(curr)
        
        return [res[i]-res[i-1] for i in range(1, len(res))]
