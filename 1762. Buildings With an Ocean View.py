
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        n = len(heights) 
        res =[n-1] 
        for i in range(n-2,-1,-1):
            building = heights[i]
            if res and building > heights[res[-1]]:
                res.append(i)
        return res[::-1]
