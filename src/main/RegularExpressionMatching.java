package main;

/**
 '.' Matches any single character.
 '*' Matches zero or more of the preceding element.

 The matching should cover the entire input string (not partial).

 The function prototype should be:
 bool isMatch(const char *s, const char *p)

 Some examples:
 isMatch("aa","a") return false
 isMatch("aa","aa") return true
 isMatch("aaa","aa") return false
 isMatch("aa", "a*") return true
 isMatch("aa", ".*") return true
 isMatch("ab", ".*") return true
 isMatch("aab", "c*a*b") return true
 */
public class RegularExpressionMatching {
    public boolean isMatch(String s, String p) {
        //Base condition: we are done
        if(p.length() == 0)
            return s.length() == 0;

        //p length 1 is a special case
        //normal case scenario without *, look ahead one char
        if(p.length() == 1 || p.charAt(1) != '*') {
            if(s.length() < 1 || p.charAt(0) != '.' && p.charAt(0) != s.charAt(0))
                return false;

            return isMatch(s.substring(1),p.substring(1));

        } else {
            //Handle * cases
            int len = s.length();
            int i = -1;
            // i < 0 to just get the loop going, and it won't do further comparison if the first
            // comparison is satisfied.
            // Be careful it is i < len, NOT i < len -1, since we shall check for length == 0
            while(i < len && ( i < 0 || p.charAt(0) == '.' || s.charAt(i) == p.charAt(0))) {

                //skip the * portion for next iteration
                //if doesn't work, increase i and try again
                //until succeed. increasing i imply letting the *
                //match more and the remaining RHS match less of the pattern
                if(isMatch(s.substring(i+1),p.substring(2)))
                    return true;

                i++;
            }
            return false; //we fail to find
        }
    }
}
