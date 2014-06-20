package main;

/**
 Container With Most Water
 Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
 Note: You may not slant the container.

 */
public class ContainerWithMostWater {
    //One way is to use the smallest can compare the max area
    //but O(N^2)
    //Better way is to start from both end and
    //advance pointer based on height until the two pointer meet
    public int maxArea(int[] height) {
        int len = height.length;
        if(len < 2) return 0;
        int max = 0;
        int r = len - 1;
        int l = 0;
        while(l<r){
            max = Math.max(max,(r-l)*Math.min(height[l],height[r]));
            if(height[l] <= height[r])
                l++;
            else
                r--;
        }
        return max;
    }

}
