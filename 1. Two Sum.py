class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        bag={}
        for i, num in enumerate(nums):
            if num in bag:  #O(1)
                return [bag[num] , i] 
            else: 
                bag[ target-num ] = i 
