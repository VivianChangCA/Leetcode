class Solution: 
    def subarraySum(self, nums: List[int], k: int) -> int:
      lookup = defaultdict(int)
      lookup[0] = 1
      total,count = 0, 0  
      
      for num in nums:
        total += num
        if total - k in lookup:
          count += lookup[total-k]
        lookup[total] += 1 
        
      return count
