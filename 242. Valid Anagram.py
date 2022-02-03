class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_map = defaultdict(int)
        t_map = defaultdict(int)
        
        for i in range(len(s)):
          s_map[s[i]] += 1 
          t_map[t[i]] += 1 
        
        for char in s_map:
          if s_map[char] != t_map.get(char, 0): return False
        
        return True
