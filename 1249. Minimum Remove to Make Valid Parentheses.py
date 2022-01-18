class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
      removelist = []
      res = list(s)
      
      for i, char in enumerate(res):
        if char == "(": 
          removelist.append(i) 
        elif char == ")": 
          if removelist: 
            removelist.pop()
          else:
            res[i] = ""
      
      for i in removelist:
        res[i] = ""
      
      return "".join(res)
