"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node):
        if not node:
            return node
        root = Node(node.val)
        stack = [node]
        visit = {}
        visit[node.val] = root
        while stack:
            top = stack.pop()

            for n in top.neighbors:
                if n.val not in visit:
                    stack.append(n)
                    visit[n.val] = Node(n.val)
                visit[top.val].neighbors.append(visit[n.val])

        return root