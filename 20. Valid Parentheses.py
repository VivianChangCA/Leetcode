class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1 : return False
        stack = []
        valid = {'(':')','{':'}','[':']' } 
        for s1 in s:
          if s1 in valid: # open 
            stack.append( s1)
          else: 
            if not stack or s1 != valid[ stack[-1] ]: # 沒有可配對的, 或者抵銷的
                 return False  
            stack.pop()  
        #return True if not stack else False
        return not stack
