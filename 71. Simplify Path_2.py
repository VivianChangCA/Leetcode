class Solution:
    def simplifyPath(self, path: str) -> str:
      stack = []
      partition = ""
      for char in path + "/":
        if char == "/":
          if partition == "..":
            if stack: stack.pop() 
          elif partition == "." or partition =="": 
            pass 
          else: 
            stack.append(partition) 
          partition = ""
        else:
          partition += char 
      return "/" + "/".join(stack)
