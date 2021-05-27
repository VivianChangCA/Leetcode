class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid)==0:
            return 0
        
        n, m = len(grid), len(grid[0])
        
        def bfsHelper(i, j):
            grid[i][j] = '0'
            queue = []
            queue.append((i,j))
            
            while queue:
                x, y = queue.pop()
                for (nx, ny) in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if (0 <= nx < n) and (0 <= ny < m):
                        if grid[nx][ny]=='1':
                            grid[nx][ny]='0'
                            queue.append((nx, ny))
                
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    bfsHelper(i, j)
                    cnt += 1
        
        return cnt
