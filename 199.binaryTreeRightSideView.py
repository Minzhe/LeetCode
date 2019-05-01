# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        if root is None: return []
        view = []
        level = [root]
        while level:
            view.append(level[-1].val)
            level = [leaf for node in level for leaf in (node.left, node.right) if leaf is not None]
        return view