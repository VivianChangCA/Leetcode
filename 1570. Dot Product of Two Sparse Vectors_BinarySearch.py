class SparseVector:
    def __init__(self, nums: List[int]):
        self.pair = [(i, val) for i, val in enumerate(nums) if val]
         
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        def binary_search(arr, low, high, target):
            while low <= high:
                mid = (low + high) // 2
                if arr[mid][0] == target:
                    return mid
                elif arr[mid][0] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return -1
        
        small_pair, long_pair = self.pair, vec.pair 
        if len(small_pair) > len(long_pair):  small_pair, long_pair =  long_pair , small_pair
        res = 0 
        j = 0
        for i, val in small_pair:   
            idx = binary_search(long_pair, j, len(long_pair) - 1, i)
            if idx != -1:
                res += val * long_pair[idx][1] 
                j = idx + 1
        return res 
