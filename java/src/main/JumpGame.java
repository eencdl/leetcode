package main;

/**
 Given an array of non-negative integers, you are initially positioned at the first index of the array.

 Each element in the array represents your maximum jump length at that position.

 Determine if you are able to reach the last index.

 For example:
 A = [2,3,1,1,4], return true.

 A = [3,2,1,0,4], return false.
 */
public class JumpGame {
    //The idea is we try to find maximum jump
    //for all possible i <= maximum jump
    //until maximum jump >= last index
    //Not possible when i > maximum jump
    public boolean canJump(int[] A) {
        if(A.length == 0) return false;
        if(A.length == 1) return true;

        int maxjump = 0;

        for(int i=0; i<A.length; i++) {
            //index must be smaller than max jump
            if(i <= maxjump) {
                //if possible, then find the next max jump
                maxjump = Math.max(maxjump,A[i]+i);

                //success
                if(maxjump >= A.length - 1)
                    return true;

            } else {
                //when i > max jump, no chance of reaching last index
                return false;
            }
        }
        return false;
    }
}
