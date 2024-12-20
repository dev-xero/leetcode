# https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements

"""
You are given an array nums consisting of positive integers.

Starting with score = 0, apply the following algorithm:

    Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest index.
    Add the value of the chosen integer to score.
    Mark the chosen element and its two adjacent elements if they exist.
    Repeat until all the array elements are marked.

Return the score you get after applying the above algorithm.
"""

import heapq as hq


class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        marked = [False] * len(nums)

        heap = []
        for i in range(len(nums)):
            hq.heappush(heap, (nums[i], i))

        while heap:
            num, idx = hq.heappop(heap)
            if not marked[idx]:
                score += num
                marked[idx] = True

                if idx + 1 < len(nums):
                    marked[idx+1] = True

                if idx - 1 > -1:
                    marked[idx-1] = True

        return score
