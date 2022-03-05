 
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.words = []
        
class Solution:
    def suggestedProducts(self, products , searchWord ) : 
        products.sort()
        root = TrieNode() 
        for product in products:
            cur = root
            for pd in product:
                cur = cur.children[pd]
                if len(cur.words) < 3:
                    cur.words.append(product) 
        res = []
        cur = root 
        for w in searchWord:
            cur = cur.children[w]
            res.append(cur.words)
        return res
