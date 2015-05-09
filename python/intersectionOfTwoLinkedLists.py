__author__ = 'don'
"""
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        # Find delta between the 2 lists
        if headA is None or headB is None:
            return None
        p1, p2 = headA, headB
        cnt1, cnt2 = 0, 0
        while p1 is not None or p2 is not None:
            if p1 is not None:
                cnt1 += 1
                p1 = p1.next

            if p2 is not None:
                cnt2 += 1
                p2 = p2.next

        diff = abs(cnt1 - cnt2)
        if cnt2 > cnt1:
            p1, p2 = headB, headA
        else:
            p1, p2 = headA, headB

        for i in range(diff):
            p1 = p1.next

        while p1 is not None:
            if p1 == p2:
                return p1
            p1, p2 = p1.next, p2.next

        return None

