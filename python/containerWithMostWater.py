__author__ = 'don'
"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
 n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
 Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.
"""
class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        lf, rg, maxV = 0, len(height)-1, 0
        while lf < rg:
            maxV = max(maxV, min(height[lf], height[rg])*(rg-lf))
            if height[lf] <= height[rg]:
                lf += 1
            else:
                rg -= 1
        return maxV


if __name__ == '__main__':
    print Solution().maxArea([1, 1])