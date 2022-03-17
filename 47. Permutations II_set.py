class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        sorted(nums)  
        n = len(nums)
        res=[]
        def helper(index):
            if index == n-1:
                res.append(tuple(nums[:]))  #unhashable type: 'list' when using built-in set function
            for i in range(index, n): 
                nums[i] , nums[index] =  nums[index], nums[i] 
                helper(index+1)
                nums[i] , nums[index] =  nums[index], nums[i] 
        helper(0)
        return set(res)
        
