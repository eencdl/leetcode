__author__ = 'don'
class Solution(object):
    def wiggleMaxLength(self, nums):
        m, l, i = 0, len(nums), 1
        if l <= 1:
            return l

        s = nums[1] > nums[0]
        n = nums[0]
        while i < l:
            if nums[i] == n:
                pass
            elif (nums[i] > n) == s:
                m += 1
                n = nums[i]
                s = not s
            else:
                if s:
                    n = min(n, nums[i])
                else:
                    n = max(n, nums[i])
            i += 1
        return m+1

print(Solution().wiggleMaxLength([0,0,0]))

