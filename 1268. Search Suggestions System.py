class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        dic = defaultdict(list)
        products.sort()  # n log n  
        for word in products:
            for i in range(len(word)):
                dic[ word[:i+1]].append(word) 
        res = []
        for i in range(len(searchWord)):  
            res.append(dic[searchWord[:i+1]][:3])
        return res 
