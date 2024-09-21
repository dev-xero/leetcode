# https://leetcode.com/problems/largest-number

"""
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.
"""


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        array = list(map(str, nums))
        array.sort(key=lambda x: x*10, reverse=True)

        # edge case
        if array[0] == '0':
            return '0'

        return ''.join(array)
