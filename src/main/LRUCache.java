package main;

import main.util.ListNode2;

import java.util.HashMap;

/**
 Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

 get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
 set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
 */
public class LRUCache {
    //storing the key -> position in lru
    HashMap<Integer,ListNode2> hm = new HashMap<Integer, ListNode2>();
    //contains value in lru
    ListNode2 head,tail;
    int max = 0;

    //Least recent use at end, most recent use at head
    public LRUCache(int capacity) {
        max = capacity;
    }

    public int get(int key) {
        if(hm.containsKey(key)) {
            ListNode2 tmp = hm.get(key);
            removeAt(tmp);
            insertAtEnd(tmp);
            return tmp.val;
        } else {
            return -1;
        }

    }

    public void set(int key, int value) {
        ListNode2 target;

        if(!hm.containsKey(key)) {
            //Add new item to LRU and table
            //adding check for max capacity
            if(hm.size() >= max && head != null) {
                //update table
                hm.remove(head.key);
                removeAt(head);
            }
            target = new ListNode2(key,value);
            hm.put(key,target);
       } else {
            //If already there, move the target

            target = hm.get(key);
            target.val = value;
            removeAt(target);
        }
        //insert at end for most recent
        insertAtEnd(target);
    }

    /****** Linked list implementation start here *****/


    public void removeAt(ListNode2 target) {
        //update head tail
        if(head == target) {
            head = target.next;
        }

        if(tail == target) {
            tail = target.prev;
        }

        //update pointer
        if(target.prev != null) {
            target.prev.next = target.next;
        }

        if(target.next != null) {
            target.next.prev = target.prev;
        }

        target.next = null;
        target.prev = null;
    }

    public void insertAtEnd(ListNode2 target) {
        if(tail != null) {
            tail.next = target;
            target.prev = tail;
        }
        tail = target;

        //in case it was an empty list
        if(head == null) {
            head = tail;
        }

    }

}
