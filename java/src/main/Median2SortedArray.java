package main;

/**
 There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays.
 The overall run time complexity should be O(log (m+n)).
 */
public class Median2SortedArray {
    public double findMedianSortedArrays(int A[], int B[]) {
        int m = A.length;
        int n = B.length;
        int k = (m+n)/2;

        //odd
        if((m+n) % 2 == 1) {
            return (double) findKthElement(A,B,k,0,m-1,0,n-1);
        } else {
            return (double) (findKthElement(A,B,k  ,0,m-1,0,n-1) +
                    findKthElement(A,B,k-1,0,m-1,0,n-1)) * 0.5;
        }
    }

    //as - a start, ae - a end, bs - b start, be - b end
    public int findKthElement(int[] A, int[] B,int k,  int as, int ae,  int bs, int be) {
        int m = ae - as + 1;
        int n = be - bs + 1;

        if (m == 0)
            return B[bs + k];

        if (n == 0)
            return A[as + k];

        if (k == 0)
            return Math.min(A[as], B[bs]);

        int aMid = k * m / (m + n);
        int bMid = k - aMid - 1;

        aMid = as + aMid;
        bMid = bs + bMid;

        if (A[aMid] > B[bMid]) {
            k = k - (bMid - bs + 1);
            ae = aMid;
            bs = bMid + 1;
        } else {
            k = k - (aMid - as + 1);
            as = aMid + 1;
            be = bMid;
        }

        return findKthElement(A, B, k, as, ae, bs, be);
    }
}
