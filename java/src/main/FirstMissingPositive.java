package main;

/**
 Given an unsorted integer array, find the first missing positive integer.

 For example,
 Given [1,2,0] return 3,
 and [3,4,-1,1] return 2.

 Your algorithm should run in O(n) time and uses constant space.
 */
public class FirstMissingPositive {
    //The description is not clear, basically the integer is from 1..n
    //there is a missing integer, which mean we won't entertain
    //integer > n or integer < 0
    //if you use sort, is N Log N
    //The key here is to exploit 1..n, so that the value of A[i] is
    // i + 1, i.e A[i] == i+1
    //We can do in place by swapping the value to the correct index
    //In a way, we are sorting in time and space complexity O(N)
    //
    public int firstMissingPositive(int[] A) {
        for(int i=0; i<A.length; i++){
            if(A[i] > 0 && A[i] <= A.length) {
                while(A[i] != i+1) {
                    //The last condition just save time swapping
                    // with itself
                    if(A[i] <= 0 || A[i] > A.length
                                 || A[A[i]-1] == A[i]) {
                        break;

                    }

                    //swap
                    int tmp = A[i];
                    A[i] = A[A[i]-1];
                    A[tmp-1] = tmp;

                }
            }
        }

        //all the elements are sorted
        //identify the missing one
        int i=0;
        for(i=0; i<A.length;i++) {
            if(A[i] != i+1)
                break;
        }
        return i+1;

    }
}
