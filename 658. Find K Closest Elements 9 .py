class Solution:
    #two pointer , time O(n)
    def findClosestElements(self, arr,k,x)  :
        lens=len(arr)
        remove= lens-k
        left, right=0, lens-1
        while remove>0 :
            if abs(arr[left]-x) > abs(arr[right]-x):
                left +=1
            else:
                right-=1 
            remove -=1 
        return arr[left:left+k]
        
  
  
