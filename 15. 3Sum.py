class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort() 
        res = []  
        for i in range(n):
            if i > 0 and nums[i] == nums[ i-1]:  continue
            left, right = i+1, n-1   
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]  
                if three_sum > 0: 
                    right -= 1
                elif  three_sum < 0: 
                    left += 1 
                else:
                    res.append([ nums[i], nums[left], nums[right]] )
                    left += 1
                    # [-2,-2,0,0,2,2] -->  [[-2,0,2],[-2,0,2]]
                    while nums[left] == nums[ left-1]  and left < right:
                        left += 1  
        return res  
