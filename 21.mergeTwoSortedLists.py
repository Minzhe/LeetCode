# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ans = ListNode(0)
        while l1 or l2:
            v1 = l1.val if l1 else float('inf')
            v2 = l2.val if l2 else float('inf')
            if v1 < v2:
                ans.next = ListNode(v1)
                ans = ans.next
                l1 = l1.next
            else:
                ans.next = ListNode(v2)
                ans = ans.next
                l2 = l2.next
        return root.next