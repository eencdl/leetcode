__author__ = 'don'
"""
Reverse linked list
"""
class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if not head:
            return head
        else:
            return self.listHelper(None,head)

    def listHelper(self, t1, t2):
        if not t2:
            return t1
        tmp = t2.next
        t2.next = t1

        return self.listHelper(t2, tmp)
