__author__ = 'don'
"""
You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
"""
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.
    def reorderList(self, head):
        # 3 step process
        # find mid point and break the list
        # reverse the second list
        # merge the 2 lists
        if head is None or head.next is None:
            return

        p1, p2 = head, head.next
        while p2.next is not None:
            p1, p2 = p1.next, p2.next
            if p2.next is None:
                break
            p2 = p2.next

        #p1 is at mid

        #reverse 2 part of the list
        t = p1.next
        p1.next = None
        p2 = self.reverse(t)

        # merge 2 list
        p1 = head
        while p1 is not None:
            t1 = p1.next
            p1.next = p2
            p1 = t1
            if p2 is None:
                break
            t2 = p2.next
            p2.next = p1
            p2 = t2

    def reverse(self, node):
        if node.next is None:
            return node
        p1 = None
        p2 = node
        while p2 is not None:
            tmp = p2.next
            p2.next = p1
            p1 = p2
            p2 = tmp
        return p1

    def printNode(self, node):
        while node is not None:
            print node.val
            node = node.next

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    Solution().reorderList(head)