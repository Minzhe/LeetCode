"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root):
        if root is None: return root
        level_order, level = [], [root]
        while level:
            level_order.append([node for node in level] + [None])
            level = [leaf for node in level for leaf in (node.left, node.right) if leaf]
        for level in level_order:
            for i in range(len(level)-1):
                level[i].next = level[i+1]
        return level_order[0][0]