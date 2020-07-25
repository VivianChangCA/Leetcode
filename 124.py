class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxVal = root.val
        def dfs( root ):
            if not root:  return 0
            left = max( 0, dfs( root.left ) )
            right = max( 0, dfs( root.right ) )
            self.maxVal = max( self.maxVal,  root.val + left + right )
            return root.val + max( left, right )
        dfs(root)
        return self.maxVal
