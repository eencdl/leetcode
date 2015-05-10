__author__ = 'don'
"""
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        #need to draw to visualize
        dummy = ListNode(0)
        dummy.next = head

        p1 = dummy
        while p1 is not None and p1.next is not None and p1.next.next is not None:
            p2 = p1.next.next
            t = p2.next
            p2.next = p1.next
            p2.next.next = t
            p1.next = p2
            p1 = p2.next
        return dummy.next
