# time O(n) Space O(n)
# int ( A/B) to avoid negative number with remainder issuee
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        pre_sign= "+"
        num = 0 
        for i,char in enumerate(s): 
            if char.isdigit():
                num = num *10 + int(char) 
            if char in {'+','-','/','*'} or i== len(s)-1:
                if pre_sign == "+":
                    stack.append(num)
                elif pre_sign == "-":
                    stack.append(-num)
                elif pre_sign == "/":
                    stack.append( int(stack.pop()/ num) )
                elif pre_sign == "*":
                    stack.append(  stack.pop()* num )
                pre_sign = char
                num = 0
        return sum(stack) 
