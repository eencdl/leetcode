package main;

import java.util.Stack;

/**
 Given an absolute path for a file (Unix-style), simplify it.

 For example,
 path = "/home/", => "/home"
 path = "/a/./b/../../c/", => "/c"

 */
public class SimplifyPath {
    // Important to note in Java String
    // == tests for reference equality.
    // .equals() tests for value equality.
    // Consequently, if you actually want to test whether two strings have
    // the same value you should use .equals()
    // == is for testing whether two strings are the same object.

    public String simplifyPath(String path) {
        Stack<String> stk = new Stack<String>();
        String tmp = new String();
        String result = new String();
        for(int i=0; i<path.length(); i++){
            switch(path.charAt(i)){
                case '/':
                    if(tmp.equals("..")) {
                        if (!stk.empty()) {
                            stk.pop();
                        }
                    } else if(tmp.length() > 0 && !tmp.equals(".")) {
                        stk.push(tmp);
                    }

                    tmp = new String();
                    break;
                default:
                    tmp += path.charAt(i);
                    break;

            }
        }

        //Important, need to do it one last time
        if(tmp.equals("..")){
            if (!stk.empty()) {
                stk.pop();
            }
        } else if (tmp.length() > 0  && !tmp.equals("."))
            stk.push(tmp);

        //Populate in backwards manner
        while(!stk.empty()) {
            result = "/" + stk.pop() + result;
        }

        return result.length() == 0 ? "/" : result;
    }
}
