class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtree: ListNode
        : Linked list 增加一個Dummy head,更改下節點
        ç TimeComplexity : All other work is constant, so the overall complexity is linear.
        ç SpaceComplexity : O(1)
        解題 https://www.youtube.com/watch?v=GfRQvf7MB3k
        """
        prehead=ListNode(-1)
        prev=prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next=l1
                l1=l1.next
            else:
                prev.next=l2
                l2=l2.next
            prev=prev.next
            
        prev.next=l1 if l1 is not None else l2
        return prehead.next
