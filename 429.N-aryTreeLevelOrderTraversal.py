"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root):
        if root is None: return []
        ans, level = [], [root]
        while level:
            ans.append([node.val for node in level])
            level = [leaf for node in level for leaf in node.children if leaf]
        return ans