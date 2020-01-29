class Solution(object):
    def leafSimilar(self, root1, root2 ): 
        def leaf(node,nums):
            if node and not node.left and not node.right:
                nums.append(node.val)
            if node.left:
                leaf(node.left,nums)
            if node.right:
                leaf(node.right,nums)
            return nums
        return leaf(root1, []) == leaf(root2,[])
