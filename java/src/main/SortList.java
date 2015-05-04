package main;

import main.util.ListNode;

/**
 Sort a linked list in O(n log n) time using constant space complexity.
 */
public class SortList {
    //Get the mid point using slow and twice as fast pointers
    public ListNode sortList(ListNode head) {
        if(head == null || head.next == null)
            return head;

        return mergeSort(head);
    }

    public ListNode mergeSort(ListNode head) {

        //base condition
        //make sure is more than 1 element to proceed
        if(head == null || head.next == null)
            return head;

        //split into 2,
        // head
        // l2
        ListNode l2 = split(head);
        ListNode r1 = mergeSort(head);
        ListNode r2 = mergeSort(l2);

        return merge(r1,r2);

    }

    public ListNode merge(ListNode l1, ListNode l2) {
        //useful for linked list, using dummy
        ListNode dummy = new ListNode(0);
        ListNode tmp = dummy;

        while(l1 != null && l2 !=null) {
            if(l1.val > l2.val) {
                tmp.next = l2;
                l2 = l2.next;
            } else {
                tmp.next = l1;
                l1 = l1.next;
            }
            tmp = tmp.next;
        }

        //remaining
        if(l1 != null) {
            tmp.next = l1;
        } else if(l2 != null) {
            tmp.next = l2;
        }
        return dummy.next;
    }

    //split return the start of list 2
    public ListNode split(ListNode head) {
        //Please take note of the initial state
        //very important
        ListNode slow = head;
        ListNode fast = head.next;

        while(fast != null && fast.next != null) {
            fast = fast.next;
            fast = fast.next;
            slow = slow.next;
        }

        //l1 is head
        //get l2
        ListNode l2 = slow.next;
        //split the list
        slow.next = null;

        return l2;
    }
}
