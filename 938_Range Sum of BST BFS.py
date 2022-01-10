class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = 0
        queue  = deque([root])  
        while queue:
            node = queue.popleft() 
            if low <= node.val <= high:
                result += node.val 
            if node.left: queue.append(node.left)
            if node.right:queue.append(node.right)
            
        return result 
