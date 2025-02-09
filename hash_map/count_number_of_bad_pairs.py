# https://leetcode.com/problems/count-number-of-bad-pairs

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        """
            You are given a 0-indexed integer array nums. A pair of indices (i, j) 
            is a bad pair if i < j and j - i != nums[j] - nums[i].

            Return the total number of bad pairs in nums.
        """
        bad_pairs = 0
        diff_map = defaultdict(int)

        for i, num in enumerate(nums):
            key = i - num

            good_pairs = diff_map[key]
            bad_pairs += i - good_pairs

            diff_map[key] += 1

        return bad_pairs
