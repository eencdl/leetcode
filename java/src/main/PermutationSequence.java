package main;

import java.util.ArrayList;

/**
 The set [1,2,3,…,n] contains a total of n! unique permutations.

 By listing and labeling all of the permutations in order,
 We get the following sequence (ie, for n = 3):

 "123"
 "132"
 "213"
 "231"
 "312"
 "321"
 Given n and k, return the kth permutation sequence.

 Note: Given n will be between 1 and 9 inclusive.
 */
public class PermutationSequence {
    //The idea here store the digit, and pull out the correspond digit
    //based on position k
    public String getPermutation(int n, int k) {
        String result = "";
        ArrayList<Integer> store = new ArrayList<Integer>();
        int m = 1; //total permutation seq
        int pos = 0;
        //put all digits into a list
        //get the total permutation seq, m
        for(int i=1;i<=n;i++) {
            store.add(i);
            m *= i;
        }

        k = k-1;
        //if total permutation seq is > 1
        while(m>1) {
            m = m/n; //next total permutation seq, with 1 less digit
            n--;
            pos = k/m; //determine the digit to select
            k = k % m; //get remaining position for remaining digits

            //select the digit
            //remove used digit
            result = result + store.get(pos);
            store.remove(pos);
        }
        return result + store.get(0);
    }
}
