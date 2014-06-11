package main;

/**
 Implement wildcard pattern matching with support for '?' and '*'.

 '?' Matches any single character.
 '*' Matches any sequence of characters (including the empty sequence).

 The matching should cover the entire input string (not partial).

 The function prototype should be:
 bool isMatch(const char *s, const char *p)

 Some examples:
 isMatch("aa","a") → false
 isMatch("aa","aa") → true
 isMatch("aaa","aa") → false
 isMatch("aa", "*") → true
 isMatch("aa", "a*") → true
 isMatch("ab", "?*") → true
 isMatch("aab", "c*a*b") → false
 */
public class WildcardMatching {
    public boolean isMatch(String s, String p) {
        int star = -1;
        int mark = -1;
        int slen = s.length();
        int plen = p.length();
        int i = 0;
        int j = 0;
        while(i<slen) {
            if(j<plen && (s.charAt(i) == p.charAt(j) || p.charAt(j) == '?')){
                //either char match or match ?
                i++;
                j++;
            } else if (j<plen && p.charAt(j) == '*') {
                //move j by 1
                //don't move i because * can mean empty space
                star = j++;
                mark = i;
            } else if (star != -1){
                //j is not moving unless there is another * next to it
                //i is moving until both char is similar in condition one
                //using star and mark to move j and i because we may got
                //2nd or 3rd....hit of star consecutively
                j = star + 1;
                i = ++mark;
            } else {
                //else no matching
                return false;
            }
        }

        //make sure we clear all for pattern
        while(j<plen && p.charAt(j) == '*')
            j++;

        return j == plen;
    }
}
