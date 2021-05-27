class Solution(object):
    def orangesRotting(self, grid): 
        stack, fresh, res = [], 0, 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    stack.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        while stack:
            newlayer = []
            for x, y in stack:
                for nx, ny in [[x, y+ 1], [x+1, y], [ x-1, y], [x, y-1]]: 
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        newlayer.append((nx, ny))
            stack = newlayer 
            if newlayer:  res += 1    #空 [] ,沒有新鮮的橘子去變熟 ,最後一次不用加 
              
        return res if not fresh else -1
