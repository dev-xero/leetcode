# https://leetcode.com/problems/single-number

"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        
        for i in range(len(nums)):
            res = res ^ nums[i]
        
        return res