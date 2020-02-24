# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.inorder = []
        self.getinorder(root)
        return self.inorder[k-1]
    
    def getinorder(self, node):
        if node:
            self.getinorder(node.left)
            self.inorder.append(node.val)
            self.getinorder(node.right)
