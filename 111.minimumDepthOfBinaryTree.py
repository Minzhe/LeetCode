# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        queue = deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if node is None:
                return level - 1
            queue.append((node.left, level+1))
            queue.append((node.right, level+1))
        return level
