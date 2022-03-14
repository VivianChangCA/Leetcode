class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r = len(board)
        c = len(board[0])
        visited = set()  
        if len(word) > r * c: return False 
        def isValid(i,j,idx):
            if idx ==0 : self.visited = set()  
            if (i,j) in self.visited: return False   
            if word[idx] != board[i][j]: return False  
            if idx == len(word) - 1 and word[idx] == board[i][j]: return True 
            for x,y  in  [  (i+1,j), (i-1,j), (i,j+1), (i, j-1) ]:  
                if x >= 0 and y >= 0 and x < r and y < c: 
                    visited.add( (i,j) )  
                    if isValid(x,y,idx+1):  return True 
            visited.remove((i,j)) 
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
  
