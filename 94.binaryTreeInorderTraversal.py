# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
<<<<<<< HEAD
    def inorderTraversal(self, root):
        if root is None: return []
        ans, stack = [], [root]
        while stack:
            root = stack.pop()
            while root:
                
=======
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.inorder = []
        self.getinorder(root)
        return self.inorder
    
    def getinorder(self, node):
        if node:
            self.getinorder(node.left)
            self.inorder.append(node.val)
            self.getinorder(node.right)
        
>>>>>>> 7fba70ee45a791e1db849fc225ecfa3c3183bf28
