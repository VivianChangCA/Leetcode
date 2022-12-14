class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        stack = [] 
        for idx, val in enumerate(T):  
            while stack and  T[stack[-1]] < val:
                low=stack.pop() 
                res[low ] = idx - low 
            stack.append(idx)
        return res
            
