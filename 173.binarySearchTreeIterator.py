# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    def __init__(self, root):
        self.tree = []
        self.appendLeftNode(root)

    def next(self):
        """
        @return the next smallest number
        """
        node = self.tree.pop()
        self.appendLeftNode(node.right)
        return node.val
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        """
        return len(self.tree) != 0
    
    def appendLeftNode(self, node):
        while node:
            self.tree.append(node)
            node = node.left
        