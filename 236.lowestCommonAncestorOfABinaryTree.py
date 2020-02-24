# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q) if root.left else None
        right = self.lowestCommonAncestor(root.right, p, q) if root.right else None
        if left and right:
            return root
        else:
            return left or right