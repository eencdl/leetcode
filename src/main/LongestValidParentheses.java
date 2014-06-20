package main;

import java.util.Stack;

/**
 Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

 For "(()", the longest valid parentheses substring is "()", which has length = 2.

 Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
 */
public class LongestValidParentheses {
    public int longestValidParentheses(String s) {
        int maxlen = 0;
        int open = 0;
        int sIndex = 0;
        Stack<Integer> stk = new Stack<Integer>();



        for(int i=0; i<s.length(); i++) {
            if(s.charAt(i) == '(') {
                if(open == 0) {
                    sIndex = i;
                }
                open++;
            } else if (s.charAt(i) == ')') {
               if(open > 0) {
                   open--;
                   maxlen = Math.max(maxlen,i-sIndex);
               } else {
                   sIndex = i+1;
               }
            }
        }
        return maxlen;
    }
}
