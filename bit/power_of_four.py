# https://leetcode.com/problems/power-of-four

"""
Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4^x.
"""

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # note:
        # hexametrical number: 0x55555555 ->
        # binary: 1010101010101010101010101010101
        return n > 0 and n & (n-1) == 0 and (n & 0x55555555) != 0