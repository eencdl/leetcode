# -*- coding: utf-8 -*-
"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order,
not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def swap(p, q):
            t = nums[p]
            nums[p] = nums[q]
            nums[q] = t

        def partitioning(l, h):
            m = (l+h)/2
            swap(m, h)
            a = b = l
            while b < h:
                if nums[b] < nums[h]:
                    swap(a, b)
                    a += 1
                b += 1
            swap(h, a)
            return a

        def runner(l, h, tk):
            if l < h:
                pk = partitioning(l, h)
                if pk == tk:
                    return nums[tk]
                elif pk > tk:
                    return runner(l, pk-1, tk)
                else:
                    return runner(pk+1, h, tk)
            elif l == h:
                return nums[l]

        return runner(0, len(nums)-1, len(nums)-k)

print Solution().findKthLargest([3, 1, 2, 4], 2)