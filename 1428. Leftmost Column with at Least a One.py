class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int: 
        rows, cols = binaryMatrix.dimensions() 
        res=cols
        mid= cols//2
        for row in range(rows):
            left=0
            right=cols-1
            while (left < right) :
                mid= (left+right ) //2   
                if binaryMatrix.get(row, mid) ==0 :
                    left= mid +1 
                else:
                    right= mid
            if binaryMatrix.get(row, left) ==1 : 
                res =min(res, left) 
        return res if res < cols else -1
        
    def leftMostColumnWithOne2(self, binaryMatrix: 'BinaryMatrix') -> int:
        # Set pointers to the top-right corner. 
        rows, cols = binaryMatrix.dimensions() 
         
        current_row = 0
        pointer = cols - 1
        
        # Repeat the search until it goes off the grid.
        while current_row < rows and pointer >= 0:
            if binaryMatrix.get(current_row, pointer) == 0:
                current_row += 1
            else:
                pointer  -= 1 
        return pointer + 1 if pointer != cols - 1 else -1
