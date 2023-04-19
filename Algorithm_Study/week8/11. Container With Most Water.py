class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        s = 0
        e = len(height) - 1
        while s < e:
            area = (e - s) * min(height[s], height[e])
            max_area = max(area, max_area)
            if height[s] < height[e]:
                s += 1
            else:
                e -= 1
        return max_area


"""
https://leetcode.com/problems/container-with-most-water/

height = [1,8,6,2,5,4,8,3,7]

area = (5 - 1) * min(8, 4) = 4 * 4 = 16
max_area = 49 > 16 = 49

넓이: (e - s) * min(height[s], height[e])
"""        