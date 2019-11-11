
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """ 
        Dict1, Dict2 = {},{}
        
        for i in s:
            if i in Dict1:
                Dict1[i] = Dict1[i] +1
            else:
                Dict1[i]=1
        
        for i in t:
            if i in Dict2:
                Dict2[i] = Dict2[i] +1
            else:
                Dict2[i]=1
                
        return Dict1== Dict2 
