__author__ = 'don'
"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number,
target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        nums.sort()
        mdiff = float('inf')
        res = 0
        for i in range(len(nums)-2):
            lf = i+1
            rg = len(nums)-1
            while lf < rg:
                sum = nums[i] + nums[lf] + nums[rg]
                if mdiff > abs(target - sum):
                    mdiff = abs(target - sum)
                    res = sum
                if sum == target:
                    return sum
                elif sum < target:
                    lf += 1
                else:
                    rg -= 1
        return res
