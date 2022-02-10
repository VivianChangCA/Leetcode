 class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]: 
        dct = defaultdict(list)
        queue = deque( [(root, 0)]) 
        while queue:
            node, i = queue.popleft()
            if not node:
                continue
            dct[i].append(node.val)
            queue.append((node.left, i-1))
            queue.append((node.right, i+1))
        return [dct[i] for i in sorted(dct)]
