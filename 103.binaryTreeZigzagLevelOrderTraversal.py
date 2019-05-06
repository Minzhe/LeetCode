# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None: return []
        ans, order = [], 1
        level = [root]
        while level:
            if order == 1:
                ans.append([node.val for node in level])
            elif order == -1:
                ans.append([node.val for node in reversed(level)])
            level = self.getnextlevel(level)
            order *= -1
        return ans
    
    def getnextlevel(self, level):
        nextlevel = []
        for node in level:
            if node.left:
                nextlevel.append(node.left)
            if node.right:
                nextlevel.append(node.right)
        return nextlevel