# https://leetcode.com/problems/continuous-subarrays

"""
You are given a 0-indexed integer array nums. A subarray of nums is called continuous if:

    Let i, i + 1, ..., j be the indices in the subarray. Then, for each pair of indices i <= i1, i2 <= j, 0 <= |nums[i1] - nums[i2]| <= 2.

Return the total number of continuous subarrays.

A subarray is a contiguous non-empty sequence of elements within an array.
"""

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        if (len(nums) == 1):
            return 1
        
        cnt = 0
        freq = {}
        lf, rt, n = 0, 0, len(nums)

        while rt < n:
            freq[nums[rt]] = freq.get(nums[rt], 0)  + 1

            while max(freq) - min(freq) > 2:
                freq[nums[lf]] -= 1
                if freq[nums[lf]] == 0:
                    del freq[nums[lf]]

                lf += 1

            cnt += rt - lf + 1
            rt += 1

        return cnt