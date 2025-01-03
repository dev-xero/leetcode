# https://leetcode.com/problems/number-of-ways-to-split-array

"""
You are given a 0-indexed integer array nums of length n.

nums contains a valid split at index i if the following are true:

    The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
    There is at least one element to the right of i. That is, 0 <= i < n - 1.

Return the number of valid splits in nums
"""


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        sol = 0

        pf = [0]*n
        pf[0] = nums[0]

        for i in range(1, n):
            pf[i] = pf[i-1] + nums[i]

        for i in range(n-1):
            if pf[i] >= pf[-1] - pf[i]:
                sol += 1

        return sol
