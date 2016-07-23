__author__ = 'don'
import collections
class Solution(object):

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        cnt= collections.defaultdict(int)
        for i in nums:
            cnt[i] += 1
        n = len(nums)
        freqlist = [[] for i in range(n+1)]
        for x in cnt:
            freqlist[cnt[x]] += [x]
        r=[]
        for i in range(n, 0, -1):
            r += freqlist[i]
        return r[:k]

print(Solution().topKFrequent([1,1,1,2,2,3],2))
