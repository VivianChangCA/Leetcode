class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:  
        queue = deque( [root])
        result = 0 
        
        while queue:
          node = queue.popleft()
          if not node: continue
          if L <= node.val <= R:
            result += node.val
          if L < node.val: queue.append(node.left)
          if node.val < R: queue.append(node.right)
          
        return result 
