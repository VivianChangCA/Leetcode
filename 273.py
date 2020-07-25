 self.res=[] 
        def intToWords(nums): 
          one = {
                1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine',
                10: 'Ten',
                11: 'Eleven',
                12: 'Twelve',
                13: 'Thirteen',
                14: 'Fourteen',
                15: 'Fifteen',
                16: 'Sixteen',
                17: 'Seventeen',
                18: 'Eighteen',
                19: 'Nineteen'
            }
          ten = {
                2: 'Twenty',
                3: 'Thirty',
                4: 'Forty',
                5: 'Fifty',
                6: 'Sixty',
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety'
            }
          tenner=0
          
          hundred,rest= divmod(nums,100)
          print(hundred,rest)
          if rest > 19 :   
            tenner,rest= divmod(rest,10) 
          if hundred:
            self.res.append(one[hundred]) 
            self.res.append('Hundred') 
          if tenner>0:
            self.res.append(ten[tenner])
          if rest>0:
            self.res.append(one[rest])
             
          
        if not num:
            return 'Zero'   
        # 1. split to 3 digits group
        billion, rest =  divmod(num,1000000000)
        million, rest =  divmod(rest,1000000)
        thousand ,rest =  divmod(rest,1000)  
         
        if billion:  
            intToWords(billion)
            self.res.append('Billion')
        if million:
            intToWords(million) 
            self.res.append('Million')  
        if thousand:
            intToWords(thousand) 
            self.res.append('Thousand')  
        if rest: 
            intToWords(rest) 
        
        return " ".join(self.res )
