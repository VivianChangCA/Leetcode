class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        self.size= 0 
        
        def dfs(x,y ):
          grid[x][y] = 0
          
          for i, j in ([x+1,y], [x-1,y], [x,y+1], [x,y-1]) :
            if 0 <= i < row and 0 <= j < col and grid[i][j] == 1 : 
              self.size += 1 
              dfs (i,j) 
              
        res= 0 
        for i in range(row): 
          for j in range(col):
            if grid[i][j] == 1 : 
              self.size = 1
              dfs(i, j) 
              res = max(res, self.size)
        return res 
        
        
