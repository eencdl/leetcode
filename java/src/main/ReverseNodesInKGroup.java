package main;

import main.util.ListNode;

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
     *
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
                //pre is just 1 node before the k group of elements needed to swap
                //basically create a gap between pre and head, i.e. head - pre = k+1
                //then do the reverse
                pre = reverse(pre,head.next); //get back the head, assign to pre
                head = pre.next;
            } else {
                head = head.next;
            }
        }
        return dummy.next; //dummy.next is the real head
    }

    public ListNode reverse(ListNode pre, ListNode next) {
        ListNode p1 = pre.next;
        ListNode p2 = p1.next;

        //basically flipping p2 to the left most
        while(p2 != next) {
            p1.next = p2.next; //skipping p2 to detach p2
            p2.next = pre.next;
            pre.next = p2;
            p2 = p1.next;
        }
        return p1;
    }
}


