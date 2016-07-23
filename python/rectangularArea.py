__author__ = 'don'
"""
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area
Assume that the total area is never beyond the maximum possible value of int.

"""
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        #check whether there is overlap
        #if overlap then calculate
        #overlap == NOT no overlap
        #no overlap
        t = (C-A) * (D-B) + (G-E) * (H-F)

        if not (E >= C or A >= G or B >= H or F >= D):
            t -= (min(D, H) - max(B, F)) * (min(C, G) - max(A, E))

        return t

print Solution().computeArea(-3, 0, 3, 4, 0, -1, 9, 2)
