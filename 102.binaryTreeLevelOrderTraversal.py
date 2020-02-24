# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        if root is None: return []
        ans, level = [], [root]
        while level:
            ans.append([node.val for node in level])
            level = [leaf for node in level for leaf in (node.left, node.right) if leaf]
        return ans