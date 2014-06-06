package main;

/**
 Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
 */
public class LongestPalindromicSubstring {
    //The idea is simple just do brute force and expand from center
    //both i and i, i+1
    public String longestPalindrome(String s) {
        if(s.length() <= 1) return s;

        String longest = s.substring(0,0);
        String tmp;
        for(int i=0; i<s.length();i++) {
            tmp = getLongest(s,i,i);
            if(tmp.length() > longest.length())
                longest = tmp;

            tmp= getLongest(s,i,i+1);
            if(tmp.length() > longest.length())
                longest = tmp;

        }
        return longest;
    }

    public String getLongest(String s, int begin, int end) {
        while(begin >= 0 && end < s.length() && s.charAt(begin) == s.charAt(end)) {
            begin--;
            end++;
        }
        //substring (beginIndex,endIndex), endIndex is not inclusive, so (1,3) means 1,2
        return s.substring(begin+1,end);
    }
}
