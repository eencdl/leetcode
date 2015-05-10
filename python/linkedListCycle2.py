__author__ = 'don'
"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Follow up:
Can you solve it without using extra space?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        p1, p2 = head, head
        while p2 is not None:
            p1 = p1.next
            p2 = p2.next
            if p2 is None:
                return None
            else:
                p2 = p2.next
            if p1 == p2:
                break
        if p2 is None:
            return None
        p1 = head
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1