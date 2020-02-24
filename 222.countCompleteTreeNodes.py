# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root):
        if root is None:
            return 0
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1