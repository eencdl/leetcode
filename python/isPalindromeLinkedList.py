# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def reverseList(p1, p2):
            tmp = p2.next
            p2.next = p1
            if tmp is None:
                return p2
            return reverseList(p2, tmp)

        if head == None or head.next == None:
            return True
        p1 = head
        p2 = head.next
        while p2.next and p2.next.next:
            p2 = p2.next.next
            p1 = p1.next

        tmp2 = p1.next
        #break the list in half
        p1.next = None
        #reverse h2 list
        h2 = reverseList(None, tmp2)

        while head and h2:
            if head.val != h2.val:
                return False
            head = head.next
            h2 = h2.next
        return True

if __name__ == '__main__':
    h = ListNode(1)
    h.next = ListNode(0)
    h.next.next = ListNode(0)
    print Solution().isPalindrome(h)


