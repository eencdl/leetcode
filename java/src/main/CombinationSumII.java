package main;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

 Each number in C may only be used once in the combination.

 Note:
 All numbers (including target) will be positive integers.
 Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
 The solution set must not contain duplicate combinations.
 For example, given candidate set 10,1,2,7,6,1,5 and target 8,
 A solution set is:
 [1, 7]
 [1, 2, 5]
 [2, 6]
 [1, 1, 6]
 */
public class CombinationSumII {
    //The idea is we just need to skip duplicate, it shall be consider since
    //we are reducing the length of candidates on next iter say 1, 1, 2 , target 2
    //on first layer iteration only the first 1 is used, 2nd 1 is skip but not next layer
    //1,2 is left, and 1 shall be pick up
    List<List<Integer>> result = new ArrayList<List<Integer>>();

    public List<List<Integer>> combinationSum2(int[] num, int target) {
        //The idea is using all possible combination recursively
        Arrays.sort(num);
        calSum(new ArrayList<Integer>(),num,0,target);
        return result;
    }

    public void calSum(List<Integer> tmpList, int[] candidates, int index, int remain) {
        //base condition
        if(remain == 0) {
            result.add(new ArrayList<Integer>(tmpList));
            return;
        }

        if(remain < 0 || index >= candidates.length)
            return;

        for(int i=index; i<candidates.length; i++) {
            tmpList.add(candidates[i]);
            calSum(tmpList,candidates,i+1,remain-candidates[i]);
            tmpList.remove(tmpList.size()-1);

            //look ahead, make sure this is done "after" the we tested the candidate
            //so that if there is only one element left, it still get registered
            while(i+1<candidates.length && candidates[i]==candidates[i+1]){
                i++;
            }
        }

    }
}
