"""
In a given grid, each cell can have one of three values:

    the value 0 representing an empty cell;
    the value 1 representing a fresh orange;
    the value 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

Example 1:

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.

Note:

    1 <= grid.length <= 10
    1 <= grid[0].length <= 10
    grid[i][j] is only 0, 1, or 2.

"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q, directions = deque(), [[1,0],[-1,0],[0,1],[0,-1]]
        fresh, levels = 0, 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2: q.append((i,j))
                if grid[i][j] == 1: fresh += 1
        
        while q:
            levels+=1
            for a in range(len(q)):
                x, y = q.popleft()
                for x1, y1 in directions:
                    if 0<=x+x1<m and 0<=y+y1<n and grid[x+x1][y+y1] == 1:
                        fresh-=1
                        grid[x+x1][y+y1] = 2
                        q.append((x+x1,y+y1))
        return -1 if fresh!=0 else max(levels-1,0)