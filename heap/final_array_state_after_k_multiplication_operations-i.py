# https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i

"""
You are given an integer array nums, an integer k, and an integer multiplier.

You need to perform k operations on nums. In each operation:

    Find the minimum value x in nums. If there are multiple occurrences of the minimum value, select the one that appears first.
    Replace the selected minimum value x with x * multiplier.

Return an integer array denoting the final state of nums after performing all k operations.
"""

import heapq


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        pq = [(val, i) for i, val in enumerate(nums)]
        heapq.heapify(pq)

        while (k > 0):
            _, i = heapq.heappop(pq)
            nums[i] *= multiplier
            heapq.heappush(pq, (nums[i], i))
            k -= 1

        return nums
