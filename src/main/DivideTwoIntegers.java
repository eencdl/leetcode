package main;

/**
 Divide two integers without using multiplication, division and mod operator.
 */
public class DivideTwoIntegers {
    //The idea is to use -
    //but too slow so we have to use >> , << to speed things up
    public int divide(int dividend, int divisor) {
        if(divisor > dividend)
            return 0;

        boolean isPositive = (dividend > 0 && divisor > 0) || (dividend < 0 && divisor < 0);
        int c = 1;
        int tmp = Math.abs(divisor);
        int tmp2 = Math.abs(dividend);
        while(tmp2 > tmp) {
            tmp = tmp << 1; //multiply by 2
            c = c << 1;
        }

        int res = 0;
        while(tmp2 >= Math.abs(divisor)) {
            while(tmp2 >= tmp) {
                tmp2 -= tmp;
                res += c;
            }
            tmp = tmp >> 1;
            c = c >> 1;

        }

        return isPositive ? res : -res;

    }
}
