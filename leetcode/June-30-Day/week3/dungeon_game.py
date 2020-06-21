"""
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.
-2 (K) 	-3 	3
-5 	-10 	1
10 	30 	-5 (P)

Note:

    The knight's health has no upper bound.
    Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
"""
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        
 
        def dfs(matrix,x,y,memo):
            m, n = len(matrix), len(matrix[0])   
            if x >= m or y >= n:
                return float('inf')

            if memo[x][y] != 0:
                return memo[x][y]

            health = float('inf')
            down = dfs(matrix, x+1, y, memo)
            right = dfs(matrix, x, y+1, memo)
            health = min(health, down, right)

            if health == float('inf'):
                if matrix[x][y] < 0:
                    health = 1 - matrix[x][y]
                else:
                    health = 1
            elif health > matrix[x][y]:
                health = health - matrix[x][y]
            else:
                health = 1

            memo[x][y] = health
            return memo[x][y]
        
        m, n = len(dungeon), len(dungeon[0])
        memo = [[0] * n for _ in range(m)]
        dfs(dungeon, 0, 0, memo)
        return memo[0][0]
        