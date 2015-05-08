__author__ = 'don'
"""
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
Try to solve it in linear time/space.
Return 0 if the array contains less than 2 elements.
You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maximumGap(self, nums):
        #the key here is to use radix sort for linear time
        #use counting sort for sorting each digit
        if len(nums) < 2:
            return 0

        nums = self.radixSort(nums)

        mg = 0
        for i in range(1, len(nums)):
            mg = max(mg, nums[i] - nums[i-1])
        return mg

    def radixSort(self, nums):
        nd = 1
        m = max(nums)
        #digit by digit
        while m/nd > 0:
            nums = self.countSort(nums, nd)
            nd *= 10
        return nums


    def countSort(self, nums, nd):
        cnt = [0]*10
        n = len(nums)
        #histogram of each number
        for i in range(n):
            cnt[(nums[i]/nd) % 10] += 1

        #accumulative sum
        for i in range(1, 10):
            cnt[i] += cnt[i-1]

        print cnt
        output = [0] * n

        #put back result
        #Because it is radix sort, the order when several numbers
        #falls under the same count bucket is crucial
        #as the num list is already partial ordered, we need to put
        #the most significant num list first, as count is in descending order
        #so in reverse not in range(n)
        for i in reversed(range(n)):
            # -1 because index start with 0
            output[cnt[(nums[i]/nd) % 10] - 1] = nums[i]
            cnt[(nums[i]/nd) % 10] -= 1
        return output


#if __name__ == '__main__':
#    print Solution().radixSort([4,2,87,1,200,58,3])

