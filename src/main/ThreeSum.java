package main;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 Problem:

 Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

 Note:
 Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
 The solution set must not contain duplicate triplets.

 For example, given array S = {-1 0 1 2 -1 -4},

 A solution set is:
 (-1, 0, 1)
 (-1, -1, 2)
 */
public class ThreeSum {
    //Brute force shall be N^3 complexity
    //First, we sort the array, N Log N, since N^2 shall be larger
    //And we shall have 2 pointers and depending on the sum of 2 integer
    //if we need a bigger number, we advance the begin pointer
    //else we decrement the end pointer
    //Another important is to avoid duplicate, we need to proceed/decrement
    //pointer if it is still the same number
    public List<List<Integer>> threeSum(int[] num) {
        List<List<Integer>> results = new ArrayList<List<Integer>>();

        if(num.length < 3)
            return results;

        Arrays.sort(num);

        for(int i=0; i<num.length-2;i++) {

            //Very Important to remove duplcate results
            if(i==0 || num[i] > num[i-1]) {
                int negate = -num[i];
                int begin = i+1;
                int end = num.length - 1;
                while(begin < end) {
                    //case 1, equate to zero
                    if(num[begin] + num[end] == negate) {
                        List<Integer> tmp = new ArrayList<Integer>();
                        tmp.add(num[i]);
                        tmp.add(num[begin]);
                        tmp.add(num[end]);
                        System.out.println(tmp.toString());
                        results.add(tmp);
                        //next
                        begin++;
                        end--;
                        //Important !! remove duplicate solution
                        while(begin < end && num[end] == num[end+1])
                            end--;

                        while(begin < end && num[begin] == num[begin-1])
                            begin++;



                    } else if (num[begin]+num[end] < negate) {
                        //Means too negative, we need a bigger number
                        //since the list is sorted, we proceed begin
                        //ptr
                        begin++;
                    } else {
                        end--;
                    }
                }
            }
        }
        return results;
    }
}
