class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = []
        for char in s:
            if res and char == res[-1]:
                res.pop()
            else:
                res.append(char) 
        return "".join(res)
