class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorder(node):
            if node:
                inorder(node.left )
                res.append(node.val  )
                inorder(node.right )
        inorder(root) 
        return res  
