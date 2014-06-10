package main;

import java.util.ArrayList;
import java.util.List;

/**
 Given a collection of numbers that might contain duplicates, return all possible unique permutations.

 For example,
 [1,1,2] have the following unique permutations:
 [1,1,2], [1,2,1], and [2,1,1].
 */
public class PermutationsII {
    List<List<Integer>> results = new ArrayList<List<Integer>>();
    //Do backtracking first
    //and then don't swap if any of the element between the swapping
    //position are the same, because they would been swap before
    //Ex
    //    211 (swap 2 (pos 0) and 1 (pos 2))
    //    between pos 0 and pos 2, num[pos 1] == num[pos 2], don't swap
    //    The reason is because say after the first swap, between pos 2 and pos 1
    //    121 and then later swap pos 1 and pos 0 ==> 112 which will be
    //    duplicated seq if we swap pos 0 and pos 2 for 211
    public List<List<Integer>> permuteUnique(int[] num) {
        List<Integer> result = new ArrayList<Integer>();
        backtracking(num,0,result);
        return results;
    }

    public void backtracking(int[] num, int begin,List<Integer> result) {
        //base condition
        if(num.length == result.size()) {
            results.add(result);
            return;
        }

        for(int i=begin; i<num.length;i++) {
            if(shouldSkip(num,begin, i))
                continue;

            swap(num,begin,i);
            ArrayList<Integer> tmp = new ArrayList<Integer>(result);
            tmp.add(num[begin]);
            backtracking(num,begin+1,tmp);
            swap(num,begin,i); //swap back
        }
    }

    public boolean shouldSkip(int[] num, int i, int j) {
        //The idea is if any of the number were the same
        //They would have swap with it before.
        while(i<j) {
            if(num[i++] == num[j])
                return true;
        }
        return false;
    }

    public void swap(int[] num, int i, int j) {
        int tmp = num[i];
        num[i] = num[j];
        num[j] = tmp;
    }
}
