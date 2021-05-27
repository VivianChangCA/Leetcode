class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid)==0:
            return 0
        
        n, m = len(grid), len(grid[0])
        
        def bfsHelper(i, j):
            grid[i][j]='0'
            stack=[]
            stack.append( (i,j))
            while stack:
              x,y = stack.pop()
              for (nx, ny) in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]: 
                     if (0 <= nx < n) and (0 <= ny < m) and grid[nx][ny]=='1':
                            grid[nx][ny]='0'
                            stack.append((nx, ny))
                  
                
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1':
                    bfsHelper(i, j)
                    cnt += 1
        
        return cnt
