class Solution:
    def isMonotonic(self, nums: List[int]) -> bool: 
        inc, dec = False, False  
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]: dec = True
            if nums[i-1] < nums[i]: inc = True 
            if inc and dec:return False
        return True 
