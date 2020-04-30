"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid)==0:
            return 0

        def dfs(i,j,rows,columns,grid):
            # check if boundary exceeded or point is 0 then backtrack
            if i<0 or j<0 or i>(rows-1) or j>(columns-1) or grid[i][j]=="0":
                return 
            
            grid[i][j] ="0"
            
            # dfs on all directions
            dfs(i-1,j,rows,columns,grid)
            dfs(i+1,j,rows,columns,grid)
            dfs(i,j+1,rows,columns,grid)
            dfs(i,j-1,rows,columns,grid)
            
        islands = 0
        rows = len(grid)
        columns = len(grid[0])
        
        for i in range(0,len(grid)):
            row = grid[i]
            for j in range(0,len(row)):
                point = row[j]
                if point=="1":
                    islands+=1
                    dfs(i,j,rows,columns,grid)
                    
        return islands
            