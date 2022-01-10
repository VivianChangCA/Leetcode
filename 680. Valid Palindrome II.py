class Solution:
    def validPalindrome(self, s: str) -> bool:  
        left, right = 0 , len(s)-1
        while left < right:
          if s[left] != s[right]:
            start_string = s[left+1:right+1] #remove head character
            end_string = s[left:right] #remove tail character
            if start_string != start_string[::-1] and end_string != end_string[::-1]:
              return False
            return True 
          left += 1 
          right -= 1 
        return True
