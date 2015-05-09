__author__ = 'don'
"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1


        head = None
        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next

        p1 = head
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                p1.next = l1
                l1 = l1.next
                p1 = p1.next
            else:
                p1.next = l2
                l2 = l2.next
                p1 = p1.next

        while l1 is not None:
            p1.next = l1
            l1 = l1.next
            p1 = p1.next

        while l2 is not None:
            p1.next = l2
            l2 = l2.next
            p1 = p1.next

        return head







