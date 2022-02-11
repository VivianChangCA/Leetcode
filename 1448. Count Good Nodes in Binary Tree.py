class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = deque( [(root, float("-inf") )])  
        res = 0 
        while queue:
            node, max_res = queue.popleft()
            if node.val >= max_res:
                res += 1 
                max_res = node.val 
            if node.left: queue.append( (node.left, max_res))
            if node.right: queue.append( (node.right, max_res) )
        return res 
