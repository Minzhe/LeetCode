# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.preorder = []
        self.getpreorder(root)
        return self.preorder
    
    def getpreorder(self, node):
        if node:
            self.preorder.append(node.val)
            self.getpreorder(node.left)
            self.getpreorder(node.right)
