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
        level = [root]
        while level:
            new_level = level + [None]
            for i in range(len(new_level) - 1):
                new_level[i].next = new_level[i+1]
            level = [leaf for node in level for leaf in (node.left, node.right) if leaf]
        return root