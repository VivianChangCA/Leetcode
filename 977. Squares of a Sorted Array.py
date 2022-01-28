class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
      left, right = 0, len(nums)-1
      res =[]
      while left <= right:
          left_value = nums[left] **2
          right_value = nums[right] **2
          if left_value > right_value:
              res.append(left_value)
              left += 1 
          else:
            res.append(right_value)
            right -=1 
      return res[::-1]
