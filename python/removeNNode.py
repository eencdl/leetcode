__author__ = 'don'
"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for singly-linked list.
#class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        if head is None:
            return

        dummy = ListNode(-1)
        dummy.next = head
        p1, p2, p3 = dummy, dummy, dummy
        while p3.next is not None:
            if n <= 0:
                p1 = p1.next

            if n <= 1:
                p2 = p2.next

            n -= 1
            p3 = p3.next

        p1.next = p2.next
        p2.next = None
        if p1 == dummy:
            return p1.next
        else:
            return head








