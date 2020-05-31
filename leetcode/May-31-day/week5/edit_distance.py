"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""
from collections import deque

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m = len(word1)
        n = len(word2)
        
        dp = [[0 for x in range(n + 1)] for x in range(m + 1)] 
        
        for i in range (0,m+1):
            for j in range (0,n+1):
                if i==0:
                    dp[i][j] = j
                elif j==0:
                    dp[i][j] = i
                elif word1[i-1]==word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
        return dp[m][n]

    def minDistanceQ(self, word1: str, word2: str) -> int:
            
            visited = set()
            q = deque([(word1, word2, 0)])
            
            while q:
                w1, w2, dist = q.popleft()
                
                if (w1, w2) not in visited:
                    visited.add((w1, w2))

                    if w1 == w2:
                        return dist

                    while w1 and w2 and w1[0] == w2[0]:
                        w1 = w1[1:]
                        w2 = w2[1:]

                    dist += 1
                    q.extend([(
                        w1[1:], w2[1:], dist), 
                        (w1, w2[1:], dist), 
                        (w1[1:], w2, dist)])
