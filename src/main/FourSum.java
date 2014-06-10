package main;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;

/**
 Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

 Note:
 Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
 The solution set must not contain duplicate quadruplets.

 For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

 A solution set is:
 (-1,  0, 0, 1)
 (-2, -1, 1, 2)
 (-2,  0, 0, 2)
 Thoughts

 A typical k-sum problem. Time is N to the poser of (k-1).

 */
public class FourSum {
    //Follow the 3Sum method but add an additional loop
    //Use Hash Set to detect duplicate
    public List<List<Integer>> fourSum(int[] num, int target) {
        List<List<Integer>> results = new ArrayList<List<Integer>>();
        HashSet<List<Integer>> hs = new HashSet<List<Integer>>();

        if(num.length < 4)
            return results;

        Arrays.sort(num);

        for(int i=0; i<num.length;i++) {
            for(int j=i+1; j<num.length;j++) {
                int begin = j + 1;
                int end = num.length - 1;
                int r = target - (num[i] + num[j]);
                while (begin < end) {
                    //case 1, equate to target remaining
                    if (num[begin] + num[end] == r) {
                        List<Integer> tmp = new ArrayList<Integer>();
                        tmp.add(num[i]);
                        tmp.add(num[j]);
                        tmp.add(num[begin]);
                        tmp.add(num[end]);
                        System.out.println(tmp.toString());
                        if(!hs.contains(tmp)) {
                            hs.add(tmp);
                            results.add(tmp);
                        }

                        //next
                        begin++;
                        end--;
                        //Important !! remove duplicate solution
                        while (begin < end && num[end] == num[end + 1])
                            end--;

                        while (begin < end && num[begin] == num[begin - 1])
                            begin++;


                    } else if (num[begin] + num[end] < r) {
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
