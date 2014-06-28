package main;

import main.util.ListNode;

/**
 Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

 Follow up:
 Can you solve it without using extra space?
 */
public class LinkedListCycleII {
    //Mathematics
    //When the slow enter the loop, fast is already k step ahead, k is the
    //length before the loop
    // t mod n = (2t + k) mod n
    // move left to the right
    // 0 = n mod n = (2t - t + k) mod n
    // n = t + k
    // t = n - k
    // t is the time when both slow and fast meet
    public ListNode detectCycle(ListNode head) {
        if(head == null || head.next == null)
            return null;

        //starting very important
        //they all start at the same point
        ListNode slow = head;
        ListNode fast = head;
        while(fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
            if(slow == fast)
                break;
        }

        if(slow != fast)
            return null;

        slow = head;
        while(slow != fast) {
            slow = slow.next;
            fast = fast.next;
        }
        return fast;
    }
}
