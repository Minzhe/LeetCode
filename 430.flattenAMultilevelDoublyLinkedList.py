
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head):
        if head is None: return None
        root = flatten = Node(val=None, prev=None, next=None, child=None)
        stack = [head]
        while stack:
            node = stack.pop()
            node.prev = flatten
            flatten.next = node
            if node.next is not None:
                stack.append(node.next)
                node.next = None
            if node.child is not None:
                stack.append(node.child)
                node.child = None
            flatten = flatten.next
        root.next.prev = None
        return root.next

