class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool: 
        st1 = set(nums)
        if len(nums) != len(st1):
            return True
        else:
            return False
