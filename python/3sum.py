__author__ = 'don'
"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order.
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        #first sort it
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            #prevent duplicate
            if i == 0 or nums[i] > nums[i-1]:
                lf = i + 1
                rg = len(nums)-1
                while lf < rg:
                    if nums[lf] + nums[rg] == -nums[i]:
                        res.append([nums[i], nums[lf], nums[rg]])
                        lf += 1
                        while nums[lf] == nums[lf-1] and lf < rg:
                            lf += 1
                        rg -= 1
                        while nums[rg] == nums[rg+1] and lf < rg:
                            rg -= 1
                    elif nums[lf] + nums[rg] < -nums[i]:
                        lf += 1
                        while nums[lf] == nums[lf-1] and lf < rg:
                            lf += 1
                    else:
                        rg -= 1
                        while nums[rg] == nums[rg+1] and lf < rg:
                            rg -= 1
        return res

if __name__ == '__main__':
    print Solution().threeSum([-1,0,1,2,-1,-4])

