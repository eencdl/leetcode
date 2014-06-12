package main;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

 The same repeated number may be chosen from C unlimited number of times.

 Note:
 All numbers (including target) will be positive integers.
 Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
 The solution set must not contain duplicate combinations.
 For example, given candidate set 2,3,6,7 and target 7,
 A solution set is:
 [7]
 [2, 2, 3]
 */
public class CombinationSum {
    //The idea is using all possible combination recursively

    List<List<Integer>> result = new ArrayList<List<Integer>>();

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        calSum(new ArrayList<Integer>(), candidates, 0, target);
        return result;
    }

    public void calSum(List<Integer> tmpList, int[] candidates, int index, int remain) {
        //base condition, since the value is sorted
        //as soon as negative we stop, and no solution
        if(remain < 0 || index >= candidates.length)
            return;

        //we got the answer
        if(remain == 0) {
            result.add(tmpList);
        }

        //we try them all
        for(int i=index;i<candidates.length;i++) {
            List<Integer> tmp = new ArrayList<Integer>(tmpList);
            tmp.add(candidates[i]);
            calSum(tmp,candidates,i,remain-candidates[i]);
        }

    }
}
