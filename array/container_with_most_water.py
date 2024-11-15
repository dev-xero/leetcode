# https://leetcode.com/problems/container-with-most-water

"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if (len(height) == 2):
            return min(height[0], height[1])

        left = 0
        right = len(height) - 1
        max_seen = 0

        while left < right:
            next_area = (right - left) * min(height[left], height[right])
            max_seen = max(max_seen, next_area)

            if height[left] < height[right]:
                left += 1
            
            else:
                right -= 1
        
        return max_seen
            