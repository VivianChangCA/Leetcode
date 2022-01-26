class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int: 
         
   
        par = [i for i in range(len(isConnected) + 1)] # parent 表
        rank = [1] * (len(isConnected) + 1)  #壓縮表
        
        def find(n):
            p = par[n] 
            while p != par[p]:  
                par[p] = par[par[p]]
                p = par[p] 
            return p
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2) 
            
            if p1 == p2: return 0  #已經訪問過，也就是建立cycle的最後一個動作
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return 1  # 合併
        
        res=[]
        n=len(isConnected)
        for i in range(n):
            for j in range(i, n):
                if i != j and isConnected[i][j]:  res.append([i,j])
                
                
        for n1, n2 in res:  
             n-= union(n1, n2) 
        
        return n
