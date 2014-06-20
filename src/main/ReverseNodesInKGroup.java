package main;

/**
 Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

 If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

 You may not alter the values in the nodes, only nodes itself may be changed.

 Only constant memory is allowed.

 For example,
 Given this linked list: 1->2->3->4->5

 For k = 2, you should return: 2->1->4->3->5

 For k = 3, you should return: 3->2->1->4->5
 */
public class ReverseNodesInKGroup {
    /**
     * Reverse a link list between pre and next exclusively
     * an example:
     * a linked list:
     * 0->1->2->3->4->5->6
     * |           |
     * pre        next
     * after call pre = reverse(pre, next)
     *
     * 0->3->2->1->4->5->6
     *          |  |
     *          pre next
     * @param pre
     * @param next
     * @return the reversed list's last node, which is the precedence of parameter next
     */
    public ListNode reverseKGroup(ListNode head, int k) {
        if(head == null || k == 1)
            return head;

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode pre = dummy; //before the reverse

        int i = 0;
        while(head != null) {
            i++;

            if(i%k == 0) {
                pre = reverse(pre,head.next); //get back the head, assign to pre
                head = pre.next;
            } else {
                head = head.next;
            }
        }
        return dummy.next;
    }

    public ListNode reverse(ListNode pre, ListNode next) {
        ListNode p1 = pre.next;
        ListNode p2 = p1.next;
        while(p2 != next) {
            pre = p2.next;
            p2.next = p1;
            p1 = p2;
            p2 = pre;
        }
        return p1;
    }
}

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
        next = null;
    }
}
