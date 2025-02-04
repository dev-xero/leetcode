# https://leetcode.com/problems/maximum-ascending-subarray-sum

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        """
            Given an array of positive integers nums, return the maximum possible
            sum of an ascending subarray in nums.

            A subarray is defined as a contiguous sequence of numbers in an array.
            A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for
            all i where l <= i < r, numsi  < numsi+1. Note that a subarray of
            size 1 is ascending.
        """
        current = nums[0]
        max_seen = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                max_seen = max(max_seen, current)
                current = 0

            current += nums[i]

        return max(max_seen, current)
