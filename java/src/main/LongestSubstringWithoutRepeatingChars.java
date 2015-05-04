package main;

import java.util.HashSet;

/**
 Given a string, find the length of the longest substring without repeating characters.
 For example, the longest substring without repeating letters for "abcabcbb" is "abc",
 which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
 */
public class LongestSubstringWithoutRepeatingChars {
    public int lengthOfLongestSubstring(String s) {
        /* This method is easy but takes a long time, because index i keep resetting
        Complexity is almost N^2

        HashMap<Character,Integer> hm = new HashMap<Character, Integer>();
        char[] c = s.toCharArray();
        int maxLen = 0;

        for(int i=0; i<s.length();i++) {
            if(!hm.containsKey(c[i])) {
                hm.put(c[i],i);
            } else {
                maxLen = Math.max(maxLen,hm.size());
                i = hm.get(c[i]);
                hm.clear();
            }
        }
        maxLen = Math.max(maxLen,hm.size());
        return maxLen;
        */
        //The second approach is better O(N)
        int i=0; //i is the starting point
        int j=0; //j is the running point
        int maxlen = 0;
        HashSet<Character> hs = new HashSet<Character>();
        char[] c = s.toCharArray();
        while(j < s.length()) {
            if(!hs.contains(c[j])) {
                hs.add(c[j]);
                maxlen = Math.max(maxlen,hs.size());
                j++;
            } else {
                //move the starting point
                hs.remove(c[i]);
                i++;
            }
        }
        return maxlen;
    }
}
