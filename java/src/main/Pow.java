package main;

/**
 Implement pow(x, n).
 */
public class Pow {
    //Think of recursive solution first
    // pow(x*x,n/2) for even n
    // x * pow(x*x,n/2) for odd n
    // Then convert it to iterative

    public double pow(double x, int n) {
        double r = 1.0;
        double y = x;
        boolean minus = (n < 0);

        n = Math.abs(n);
        while(n > 0) {
            //notice the "order" very important

            //Do odd first
            //This take care of odd power i.e. 3 = 1 + 2
            //Also this take care of the last step
            //combining y and r when n == 1
            if(n % 2 == 1) {
                //This has to be stored separately
                //because it is used at the end
                r *= y;
            }

            //y is square power accumulator
            y *= y;
            n /= 2;
        }
        return minus ? 1.0/r : r;
    }
}
