class Solution:
    def maxArea(self, height: List[int]) -> int:
        right = len(height) - 1
        left = 0
        max_container = 0
        while(left < right):
            max_container = max([max_container, min(height[right], height[left]) * abs(right-left)])
            if height[left] > height[right]:
                right -=1
            else:
                left += 1
        return max_container
