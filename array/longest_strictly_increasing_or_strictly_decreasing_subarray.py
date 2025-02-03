# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        """
            You are given an array of integers nums. Return the length of the longest subarray
            of nums which is either strictly increasing or strictly decreasing.
        """

        N = len(nums)
        if N == 1:
            return N

        sub = 1

        for i in range(1, N):
            curr = 1
            increasing = nums[i] > nums[i-1]

            for j in range(i, N):
                if increasing and nums[j-1] >= nums[j]:
                    break

                if not increasing and nums[j] >= nums[j-1]:
                    break

                curr += 1

            sub = max(sub, curr)

        return sub
