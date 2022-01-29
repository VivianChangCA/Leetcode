"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        clone = {}
        clone[node] = Node(node.val)
        queue = deque([node])
        while queue:
          cur_node = queue.popleft() 
          for neighbor in cur_node.neighbors:
              if neighbor not in clone :
                clone[neighbor] = Node(neighbor.val)
                queue.append(neighbor)
              clone[cur_node].neighbors.append(clone[neighbor])
        return clone[node]
        
