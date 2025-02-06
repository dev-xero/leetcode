# https://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        """
            Given an array nums of distinct positive integers, return the number of tuples 
            (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, 
            and a != b != c != d.
        """
        N = len(nums)
        pairs = defaultdict(int)
        res = 0

        for i in range(N):
            for j in range(i+1, N):
                product = nums[i] * nums[j]
                res += 8 * pairs[product]
                pairs[product] += 1

        return res
