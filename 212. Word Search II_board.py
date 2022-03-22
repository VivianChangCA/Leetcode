class TireNode():
    def __init__(self):
        self.children = defaultdict(TireNode)
        self.isword = False
    def insert(self, word):
        cur = self
        for char in word: 
            cur = cur.children[char]   
        cur.isword = True 
        
class Solution:    
	def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
		root = TireNode()
		for word in words:
			root.insert(word)
		res = set()
		r, c = len(board), len(board[0]) 

		def dfs(row,col,node,word):  
			cell = board[row][col] 
			if cell not in node.children: return 
			word += cell
			node = node.children[cell]
			 
			if node.isword:
			    res.add(word )
			    if len(node.children)==0: return 
			     
			board[row][col] = "#"
			for x,y in [(row+1, col), (row-1, col), (row, col+1),(row, col-1)]:
			    if x < 0 or y <0 or x ==r or y == c :  continue 
			    if board[x][y] =="#" : continue
			    dfs(x, y, node, word)  
			board[row][col] = cell 

		for row in range(r):
			for col in range(c):
				if board[row][col] in root.children: 
				    dfs(row,col,root,"") #call froom each starting position and word is gonna be empty

		return list(res) #cast to list as result is a set
