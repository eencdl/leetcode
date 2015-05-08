__author__ = 'don'
"""
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        if head is None:
            return None

        prev = None
        p = head
        while p is not None:
            if p.val == val:
                if prev is None:
                    head = p.next
                    p.next = None
                    p = head
                else:
                    prev.next = p.next
                    p.next = None
                    p = prev.next
            prev = p
            p = p.next
        return head            
