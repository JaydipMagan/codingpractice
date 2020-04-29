class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid)==0:
            return 0
        
        # time limit exceeded for this approach
        def dfs(x,y):
            if x>m-1 or y>n-1:
                return inf
            if x==m-1 and y==n-1:
                return grid[y][x]
            
            bottom = dfs(x,y+1)
            right = dfs(x+1,y)
            point = grid[y][x]
            
            return min(point+right,point+bottom)
        
        m = len(grid[0])
        n = len(grid)
        
        # mini = dfs(0,0)
        # return mini
        for i in range(0,m):
            for j in range(0,n):
                current = grid[j][i]
                if i==0 and j==0:#skip first cell
                    continue 
                    
                if j==0:#first row
                    grid[j][i] = current+grid[j][i-1] # current value + left cell value
                elif i==0:#first col
                    grid[j][i] = current+grid[j-1][i] # current value + above cell value
                else:
                    grid[j][i] = min(current+grid[j-1][i],current+grid[j][i-1]) # which ever one gives min sum
                    
        return grid[n-1][m-1]       
                    
                    
                    