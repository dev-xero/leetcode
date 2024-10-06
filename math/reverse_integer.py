# https://leetcode.com/problems/reverse-integer


"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""


class Solution:
    def reverse(self, x: int) -> int:
        res, MAX = 0, -(2**31)

        sign = 1 if x > 0 else -1
        x = abs(x)

        while x != 0:
            q = int(x % 10)

            if (res > MAX // 10) or (res == MAX // 10 and q > 7):
                return 0

            res = res * 10 + q
            x //= 10

        return sign * res
