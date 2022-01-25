class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        p1, p2 = 0, 0
        power = 0 
        num = 0  
        while p1 < len(word) and p2 < len(abbr):
            if abbr[p2].isdigit():   
                while p2 < len(abbr) and abbr[p2].isdigit():
                    if num == 0 and int(abbr[p2]) == 0:  
                        return False  #  leading zeros 
                    num = 10*num + int(abbr[p2])
                    p2 += 1 
                p1 += num   
                num = 0  
            else:
                if abbr[p2] != word[p1]: return False
                p1 += 1
                p2 += 1
        
        return len(word) == p1 and len(abbr) == p2 
