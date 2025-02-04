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

    def longestMonotonicSubarrayQ(self, nums: List[int]) -> int:
        """
        Same problem, optimized - O(n)
        """
        N = len(nums)
        incLength, decLength = 1, 1
        maxLength = 1

        for i in range(1, N):
            if nums[i] > nums[i-1]:
                incLength += 1
                decLength = 1

            elif nums[i-1] > nums[i]:
                decLength += 1
                incLength = 1
            
            else:
                incLength = 1
                decLength = 1
            
            maxLength = max(maxLength, incLength, decLength)

        return maxLength