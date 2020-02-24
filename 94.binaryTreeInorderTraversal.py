# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        if root is None: return []
        ans, stack = [], [root]
        while stack:
            root = stack.pop()
            while root:
                