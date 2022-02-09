class SparseVector:
    def __init__(self, nums: List[int]):
        self.pair = [ [i, val] for i, val in enumerate(nums) if val]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0 
        p1, p2 = 0, 0  
        while p1 < len(self.pair) and p2 < len(vec.pair):
            if self.pair[p1][0] == vec.pair[p2][0]: 
                res += self.pair[p1][1] *  vec.pair[p2][1] 
                p1 += 1 
                p2 += 1
            elif self.pair[p1][0] > vec.pair[p2][0]:
                p2 += 1 
            else:
                p1 += 1 
        return res 
