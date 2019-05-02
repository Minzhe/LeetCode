# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.inorder = []
        self.getinorder(root)
        return self.inorder
    
    def getinorder(self, node):
        if node:
            self.getinorder(node.left)
            self.inorder.append(node.val)
            self.getinorder(node.right)
        
