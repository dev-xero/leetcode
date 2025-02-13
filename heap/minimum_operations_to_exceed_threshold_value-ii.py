# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        """
            You are given a 0-indexed integer array nums, and an integer k.

            In one operation, you will:

                Take the two smallest integers x and y in nums.
                Remove x and y from nums.
                Add min(x, y) * 2 + max(x, y) anywhere in the array.

            Note that you can only apply the described operation if nums contains 
            at least two elements.

            Return the minimum number of operations needed so that all elements of 
            the array are greater than or equal to k.
        """
        heapq.heapify(nums)
        ops = 0

        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            z = min(x, y) * 2 + max(x, y)

            heapq.heappush(nums, z)
            ops += 1

        return ops