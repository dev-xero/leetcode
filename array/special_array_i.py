# https://leetcode.com/problems/special-array-i

"""
An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.
"""


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if (nums[i-1] & 1 == nums[i] & 1):
                return False

        return True
