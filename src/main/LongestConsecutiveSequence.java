package main;

import java.util.HashSet;

/**
 Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

 For example,
 Given [100, 4, 200, 1, 3, 2],
 The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

 Your algorithm should run in O(n) complexity.
 */
public class LongestConsecutiveSequence {
    //One way is to sort but that takes N log N
    //so use HashSet and the key is to remove the ones
    //already consider
    public int longestConsecutive(int[] num) {
        HashSet<Integer> hs = new HashSet<Integer>();
        for(int n : num) {
            hs.add(n);
        }
        int max = 0;
        for(int n : num) {
            int left = n-1; //expand left
            int right = n+1; //expand right
            int cnt = 1; //one for current element

            while(hs.contains(left)){
                cnt++;
                hs.remove(left); //this is key, to not consider again
                left--;
            }

            while(hs.contains(right)) {
                cnt++;
                hs.remove(right);
                right++;
            }
            max = Math.max(max,cnt);

        }
        return max;
    }


}
