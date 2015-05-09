"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
"""
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        #little trick 3 reverses are equal to rotate
        n = len(nums)
        if n == 0:
            return

        k %= n
        if k != 0:
            self.reverse(nums, 0, n-1)
            print nums
            self.reverse(nums, 0, k-1)
            print nums
            self.reverse(nums, k, n-1)
        return nums

    def reverse(self,nums, s, e):
        for i in range((e-s+1)/2):
            tmp = nums[s+i]
            nums[s+i] = nums[e-i]
            nums[e-i] = tmp
        return nums



if __name__ == '__main__':
    print Solution().rotate([1,2,3,4], 2)
