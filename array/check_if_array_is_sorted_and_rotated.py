#

"""
Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.
"""


class Solution:
    def check(self, nums: List[int]) -> bool:
        """
            Linear time complexity, O(1) extra space.
        """

        N = len(nums)
        inversions = 0

        for i in range(1, N):
            if nums[i] < nums[i-1]:
                inversions += 1

        if nums[0] < nums[N-1]:
            inversions += 1

        return inversions <= 1

    def checkQ(self, nums: List[int]) -> bool:
        """
            Quadratic time complexity, O(N) extra space.
        """

        N = len(nums)
        sorted_nums = sorted(nums)
        nums += nums

        for i in range(N*2):
            if nums[i:N+i] == sorted_nums:
                return True

        return False
