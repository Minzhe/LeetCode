# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def closestValue(self, root, target):
        if root is None:
            return float('Inf')
        else:
            left = self.closestValue(root.left, target)
            right = self.closestValue(root.right, target)
            diff = [(abs(left - target), left), (abs(root.val - target), root.val), (abs(right - target), right)]
            diff = sorted(diff, key=lambda x: x[0])
            return diff[0][1]
