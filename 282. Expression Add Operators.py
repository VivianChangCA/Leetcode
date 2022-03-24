class Solution:
    def addOperators(self, s: str, target: int) -> List[str]:
        def backtrack(i, path, resultSoFar, prevNum):
            if i == len(s) and resultSoFar == target:
                ans.append(path)
                return

            for j in range(i, len(s)):
                if j > i and s[i] == '0': break  # Skip leading zero number
                num = int(s[i:j + 1])  
                str_num = s[i:j+1] 
                int_num = int(str_num)
                if i == 0: 
                    backtrack(j+1, str_num , int_num, int_num)
                     
                else:
                    backtrack(j+1, path + "+" + str_num , resultSoFar + int_num, int_num) 
                    backtrack(j+1, path + "-" + str_num , resultSoFar - int_num, -int_num) 
                    backtrack(j+1, path + "*" + str_num , resultSoFar - prevNum + prevNum *int_num, prevNum *int_num)  

        ans = []
        backtrack(0, "", 0, 0)
        return ans
# case 1    
# "105"
# 5
# ["1*0+5","10-5"]
