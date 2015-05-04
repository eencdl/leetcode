package main;

/**
 Given an array of non-negative integers, you are initially positioned at the first index of the array.
 Each element in the array represents your maximum jump length at that position.
 Your goal is to reach the last index in the minimum number of jumps.
 For example:
 Given array A = [2,3,1,1,4]
 The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

 */
public class JumpGameII {
    //The idea here is to use Greedy algorithm, because greediness, covers all the range
    //For example
    //2,3,1,100,3
    //at index 0, 2, you can jump to 3 or 1, you choose 3, it will still hit 100
    //remember it is the maximum it can jump, but doesn't mean it has to jump the max
    public int jump(int[] A) {
        int i = 0;
        int n = A.length - 1;
        int cnt = 0;
        int m = 0;

        while(i < n) {
            m = A[i]+i;
            cnt++;
            if(m >= n)
                return cnt;

            int tmp = 0;
            //Find max for next jump
            for(int j=i+1;j<=m;j++) {
                if(j+A[j] > tmp) {
                    tmp = j+A[j];
                    i = j;
                }
            }

        }
        return cnt;
    }
}
