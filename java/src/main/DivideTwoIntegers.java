package main;

/**
 Divide two integers without using multiplication, division and mod operator.
 */
public class DivideTwoIntegers {
    //Main idea is to use - but need to speed up by using <<
    //since it is multiply by 2 for left shift
    public int divide(int dividend, int divisor) {
        if(divisor == 0)
            return 0;
        /*
 Integer.MIN_VALUE is -2147483648, but the highest value a 32 bit integer can contain is +2147483647.
 Attempting to represent +2147483648 in a 32 bit int will effectively "roll over" to -2147483648.
 This is because, when using signed integers, the two's complement binary representations of
 +2147483648 and -2147483648 are identical. This is not a problem, however, as +2147483648
 is considered out of range.
 So USING LONG TYPE is crucial in passing the test
 */
        long a = Math.abs((long)dividend);
        long b = Math.abs((long)divisor);
        long result = 0;
        while (a >= b) {
            long c = b;
            int i = 0;
            while(a >= c) {
                a -= c;
                c = c<<1;
                result += 1<<i;
                i++;
            }
        }

        if((dividend > 0 && divisor < 0) || (dividend < 0 && divisor > 0))
            result = -result;

        return (int)result;
    }
}
