package main;

/**
 Implement atoi to convert a string to an integer.

 Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

 Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
 */
public class Atoi {
    public int atoi(String str) {
        str = str.trim();
        if(str.length() == 0)
            return 0;

        int i = 0;
        boolean isPositive = true;
        if(str.charAt(i) == '-') {
            i++;
            isPositive = false;
        } else if (str.charAt(i) == '+') {
            i++;
        }

        //usig double is crucial to remove overflow
        double res = 0;
        while(i < str.length() && str.charAt(i) >= '0' && str.charAt(i) <= '9') {
            res = res*10 + (str.charAt(i) - '0');
            i++;
        }

        if(isPositive) {
            if(res > Integer.MAX_VALUE) {
                return Integer.MAX_VALUE;
            }
        } else {
            res = -res;
            if(res < Integer.MIN_VALUE) {
                return Integer.MIN_VALUE;
            }
        }
        return (int)res;
    }
}
