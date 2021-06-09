class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
      songs=defaultdict(int)
      res=0
      for timeI in time:
        timeI= timeI % 60  
        if timeI==0 :
          res += songs[timeI] 
        else:
          num= 60-timeI
          res += songs[num] 
        songs[timeI]+=1
      return res 
          
