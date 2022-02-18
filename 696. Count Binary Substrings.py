class Solution:
    def countBinarySubstrings(self, s: str) -> int: 
        pre, cur, ans = 0, 1, 0  
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur += 1 
            else: 
                ans += min(pre, cur)  
                pre, cur = cur, 1 
        return ans + min(pre, cur)
