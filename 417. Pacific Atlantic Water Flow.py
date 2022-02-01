class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
      rows, cols = len(heights), len(heights[0])
      pac_visit, atl_visit = set(), set()
      
      def dfs(x,y, pre_height, visit):
         if (x,y) not in visit and x >= 0 and y >= 0 and x < rows and y < cols and heights[x][y]  >= pre_height :
          visit.add( (x,y))
          dfs(x+1, y, heights[x][y], visit) 
          dfs(x-1,y, heights[x][y], visit) 
          dfs(x,y+1, heights[x][y], visit) 
          dfs(x,y-1, heights[x][y], visit) 

      for x in range(rows):
        dfs(x, 0,  heights[x][0],pac_visit)
        dfs(x, cols-1,  heights[x][cols-1], atl_visit)
        
      for y in range(cols):
        dfs(0,y,  heights[0][y],pac_visit)
        dfs(rows-1,y,  heights[rows-1][y], atl_visit)  
      
      # find overlapping cells
      res=[]
      for x in range( rows):
        for y in range( cols):
          if (x,y) in pac_visit and (x,y) in atl_visit:
              res.append([x,y])
      
      return res 
