# Time complexity : O(\log n +k)O(logn+k). O(\log n)O(logn) is for the time of binary search, while O(k)O(k) is for shrinking the index range to k elements.
# detail explantion  https://leetcode-cn.com/problems/search-insert-position/solution/te-bie-hao-yong-de-er-fen-cha-fa-fa-mo-ban-python-/
def findClosestElements(self, arr,k,x)  :
        size = len(arr)
        left = 0
        right = size - k

        while left < right:
            # mid = left + (right - left) // 2
            mid = (left + right) >> 1
           
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]
