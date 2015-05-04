package main;

/**
 Given a sorted array of integers, find the starting and ending position of a given target value.

 Your algorithm's runtime complexity must be in the order of O(log n).

 If the target is not found in the array, return [-1, -1].

 For example,
 Given [5, 7, 7, 8, 8, 10] and target value 8,
 return [3, 4].
 */
public class SearchRange {
    //Simple binary search problem, corner case makes it hard
    //need to think carefully for corner case
    public int[] searchRange(int[] A, int target) {

        if(A.length == 0) return new int[]{-1,-1};

        return binarySearch(A,target,0,A.length-1);
    }

    public int[] binarySearch(int[] A, int target, int begin, int end) {

        int mid = (begin + end)/2;

        //This is the best way to check for
        //base condition, since begin and end
        //shall always increment or decrement
        if(end < begin)
            return new int[]{-1,-1};

        if(A[mid] == target) {
            //once found we need to expand left / right
            //search to determine the boundary
            int a = mid;
            //make sure is >=0 not > 0, boundary case
            while(a-1 >= 0 && A[a-1] == target)
                a--;

            int b = mid;
            while(b+1 < A.length && A[b+1] == target)
                b++;

            return new int[]{a,b};

        } else if (A[mid] > target) {
            //Here putting mid-1 instead of mid is crucial !!
            //because that avoid infinite loop, it ensure
            //end is always decrementing
            return binarySearch(A,target,begin,mid-1);
        } else {
            //Here putting mid+1 instead of mid is crucial !!
            //because that avoid infinite loop, it ensure
            //begin is always increasing
            return binarySearch(A,target,mid+1,end);
        }

    }

}
