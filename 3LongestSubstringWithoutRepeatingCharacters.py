class Solution:
     
    def lengthOfLongestSubstring(self, s: str) -> int:
        #1. two pointer 
        if not s : return 0
        lookup={}
        res,left=0,0
        for right, ch in enumerate(s):
          if ch in lookup: 
            if left <= lookup[ch]  :
                left=lookup[ch]+1  
            
          res=max(res, right-left+1) 
          lookup[ch]=right
        return max(res, right-left+1)
