
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        p1,p2 讀取各別資料的位置
        p 實際放置位置
        從後尾數開始讀取比較大小, nums1[p1]< nums2[p2]  就到到右邊,  比較小的時候 就移出空格
        """
        p1=m-1
        p2=n-1
        p=m+n-1
        
        while p1>= 0 and p2>= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p]=nums2[p2]
                p2 -=1
            else:
                nums1[p]=nums1[p1]
                p1 -=1
            p-= 1
         
        nums1[:p2+1]=nums2[:p2+1]
        
