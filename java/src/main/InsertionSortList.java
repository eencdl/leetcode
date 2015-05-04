package main;

import main.util.ListNode;

/**
 Sort a linked list using insertion sort.
 */
public class InsertionSortList {
    //Linked list always use dummy ptr
    //the trick here is to compare and swap the "next" element
    //not the current element.
    public ListNode insertionSortList(ListNode head) {
        if(head == null || head.next == null)
            return head;

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode insert = head;

        //Iterate until the end
        while(insert != null && insert.next != null) {
            head = dummy;
            //iterate until insert pointer
            while(head.next != insert.next) {
                if(head.next.val > insert.next.val) {
                    //found and insert
                    ListNode tmp = head.next;
                    head.next = insert.next;
                    insert.next = insert.next.next;
                    head.next.next = tmp;
                    break;
                }
                head = head.next;
            }
            //We don't have to move the insert pointer
            //If there is an insert since insert is
            //"move" if there is a swap
            //if no swap, then move the insert ptr
            if(head.next == insert.next)
                insert = insert.next;
        }
        return dummy.next;
    }
}
