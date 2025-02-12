# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits

class Solution:
    def digit_sum(self, num) -> int:
        res = 0

        while num:
            res += num % 10
            num //= 10

        return res

    def maximumSum(self, nums: List[int]) -> int:
        """
            You are given a 0-indexed array nums consisting of positive integers. 
            You can choose two indices i and j, such that i != j, and the sum of 
            digits of the number nums[i] is equal to that of nums[j].

            Return the maximum value of nums[i] + nums[j] that you can obtain 
            over all possible indices i and j that satisfy the conditions.
        """
        sum_groups = defaultdict(list)

        for num in nums:
            digit_sum = self.digit_sum(num)
            sum_groups[digit_sum].append(num)
        
        max_eqsum = -1
        for k, v in sum_groups.items():
            largest = max(v)
            v.remove(largest)
            if not v:
                continue

            second_largest = max(v)
            max_eqsum = max(max_eqsum, largest + second_largest)

        return max_eqsum
        