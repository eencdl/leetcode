package main;

/**
 Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
 For example,
 Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


 */
public class TrappingRainWater {
    //The idea is to calculate the maximum from left to right (delay by 1)
    //and calculate maximum from right to left (delay by 1)
    //This is to form left and right wall for each column of water
    public int trap(int[] A) {
        int n = A.length;

        if(n==0)
            return 0;

        int[] maxL = new int[n];
        int[] maxR = new int[n];
        int max = A[0];
        maxL[0] = 0;
        //finding maximum wall from left
        //delay by 1
        for(int i=1;i<n-1;i++) {
            maxL[i] = max;
            if(A[i] > max)
                max = A[i];
        }
        maxR[n-1] = 0;
        max = A[n-1];

        //finding maximum wall from right
        //delay by 1
        int totaltrap = 0;
        int tmptrap = 0;
        for(int i=n-2;i>0;i--) {
            maxR[i] = max;
            //calculate the amount of water for 1 column
            tmptrap = Math.min(maxR[i],maxL[i]) - A[i];

            //only add if it is positive, negative would mean
            //there is no wall to support the water
            if(tmptrap > 0)
                totaltrap += tmptrap;

            if(A[i] > max)
                max = A[i];
        }
        return totaltrap;
    }
}
