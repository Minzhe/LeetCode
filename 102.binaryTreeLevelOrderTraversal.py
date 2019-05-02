# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None: return []
        ans, level = [], [root]
        while level:
            ans.append([node.val for node in level])
            level = self.getnextlevel(level)
        return ans
            
    def getnextlevel(self, level):
        nextlevel = []
        for node in level:
            if node.left:
                nextlevel.append(node.left)
            if node.right:
                nextlevel.append(node.right)
        return nextlevel
        
