class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :對照組i 
        :實驗組j 
        :當對照組和實驗組不同時  將實驗組存到對照組隔壁 (i+1的位置)
        
        """
        if nums==[] or nums is None :
            return False
        i = 0
        for j in range(1,len(nums) ):
            if nums[i]  != nums[j]:
                i+=1
                nums[i] = nums[j] 
        return i+1
