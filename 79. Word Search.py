class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r = len(board)
        c = len(board[0])
        self.visited = set()  
        if len(word) > r * c: return False # case1
        def isValid(i,j,idx):
            if idx ==0 : self.visited = set()  
            if (i,j) in self.visited: return False   
            if word[idx] != board[i][j]: return False  
            if idx == len(word) - 1 and word[idx] == board[i][j]: return True 
            for x,y  in  [  (i+1,j), (i-1,j), (i,j+1), (i, j-1) ]:  
                if x >= 0 and y >= 0 and x < r and y < c: 
                    self.visited.add( (i,j) )  
                    if isValid(x,y,idx+1):  return True 
            self.visited.remove((i,j))  # case2: 當前字是符合，可是擴展四個方向的鄰居後，沒有符合的。
            return False  # 四個角都不成立時候會回傳 
        
        for i in range(r):
            for j in range(c):   
                if board[i][j] == word[0] and isValid(i, j, 0 ): 
                    return True 
        return False
    
    #case 1": [["a"]]
    #"ab" 
    # case 2: [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
    # "ABCESEEEFS"class Solution:
  
