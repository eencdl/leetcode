package main;

import main.util.ListNode;

/**
 Given a singly linked list L: L0→L1→…→Ln-1→Ln,
 reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

 You must do this in-place without altering the nodes' values.

 For example,
 Given {1,2,3,4}, reorder it to {1,4,2,3}.
 */
public class ReorderList {
    public void reorderList(ListNode head) {
        if(head == null || head.next == null || head.next.next == null)
            return;


        //First get mid point
        ListNode slow = head;
        ListNode fast = head.next;
        while(fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }

        //slow is at the end of 1st list
        //reverse the mid section of the list
        slow.next = reverse(slow.next);
        ListNode current = head;
        while(current != slow && current.next != null) {
            ListNode tmp = current.next;
            current.next = slow.next;
            slow.next = slow.next.next;
            current.next.next = tmp;
            current = tmp;
        }
        return;
    }

    public ListNode reverse(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode current = head;
        //Please note that the current ptr has
        //move through the swap
        while(current.next != null) {
            //Remember always have a tmp variable
            ListNode tmp = dummy.next;
            dummy.next = current.next;
            current.next = current.next.next;
            //Previously I had dummy.next.next = current,
            //Which is wrong since it moves
            dummy.next.next = tmp;
        }
        return dummy.next;
    }
}
