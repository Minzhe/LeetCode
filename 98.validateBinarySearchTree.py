# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        self.inorder = []
        self.getInOrder(root)
        for i in range(1, len(self.inorder)):
            if self.inorder[i] <= self.inorder[i-1]:
                return False
        return True

    def getInOrder(self, node):
        if node is not None:
            self.getInOrder(node.left)
            self.inorder.append(node.val)
            self.getInOrder(node.right)


