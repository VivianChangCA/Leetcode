class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int: 
        n = len(isConnected) 
        visited = set()
        def dfs(node_view): 
            for i, val in enumerate(isConnected[node_view]):
                if val ==1 and i not in visited:
                    visited.add(i)
                    dfs(i) 
        ans = 0
        for i in range(n):  
            if i not in visited: 
                dfs(i)  
                ans += 1 
        return ans
