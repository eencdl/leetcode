package main;

import java.util.Stack;

/**
 Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

 For "(()", the longest valid parentheses substring is "()", which has length = 2.

 Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
 */
public class LongestValidParentheses {
    //Need to use stack, think of a few scenarios
    // ()()  4
    // (()() 4
    // ())() 2
    // The main key in solving this problem is to calculate the distance between last  open '('
    // in the stack without a close ')', i.e.
    // ( ( ) has indexes 0,1,2, so 2-0 = 2, which is similar to 2 - 1 + 1
    // this is the key in solving the problem since it keep track of the valid so far
    // in cases where there are non on the stack ( ) ( ) ( ), we just compare with the first
    // valid ptr
    public int longestValidParentheses(String s) {
        if(s.length() < 2)
            return 0;
        int maxlen = 0;
        Stack<Integer> stk = new Stack<Integer>();
        for(int i=0; i < s.length(); i++) {
            if(s.charAt(i) == '(') {
                stk.push(i);
            } else {
                // ')' is captured
                if(stk.empty()) {
                    //Handle ( ) ) ) ( ) case
                    //restart ref after num of ) is more than (
                    firstValid = i+1;
                } else {
                    stk.pop();
                    if(!stk.empty()) {
                        //This line is the key !!
                        //basically only compare with the '(' the last
                        //that is not closed ')', this cater for the + 1
                        //to calculate the distance
                        //this handle the cases
                        // ( ( ) ( )
                        // ( ) ( ( ( ( ) ( ( ) )
                        maxlen = Math.max(maxlen, i - stk.peek());
                    }  else {
                        // Handle the case of
                        // ( ) ( ( ) )
                        maxlen = Math.max(maxlen, i - firstValid + 1);
                    }
                }
            }
        }
        return maxlen;
    }
}
