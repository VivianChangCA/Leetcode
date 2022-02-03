class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      count = defaultdict(list) 
      for s in strs: 
        code_list = [0] * 26  
        for char in s: 
          code_list[ ord(char) - ord('a')  ] +=1 
        count[tuple(code_list)].append(s) 
      return count.values()
          
