package main;

import java.util.Arrays;

/**
 * Created by don on 6/8/14.
 */
public class ThreeSumClosest {//This is easy same concept
    public int threeSumClosest(int[] num, int target) {
        int min = Integer.MAX_VALUE;
        int nearSum = 0;

        Arrays.sort(num);
        for(int i=0; i<num.length; i++) {
            int begin = i+1;
            int end = num.length - 1;
            while(begin < end) {
                int sum =  num[i] + num[begin] + num[end];
                //Be really careful with the diff since
                //if target is negative, sum is positive
                //you will get the wrong result,
                //MUST use absolute
                int diff = Math.abs(target - sum);
                if(diff < min) {
                    min = diff;
                    nearSum = sum;
                }

                if(sum <= target) {
                    begin++;
                } else {
                    end--;
                }
            }
        }
        return nearSum;
    }
}
