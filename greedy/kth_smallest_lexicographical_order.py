# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order

"""
Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].
"""

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_steps(curr, limit):
            steps = 0
            first = curr
            next = curr + 1
            while first <= limit:
                steps += min(limit + 1, next) - first
                first *= 10
                next *= 10
            return steps
        
        curr = 1
        k -= 1

        while k > 0:
            steps = count_steps(curr, n)
            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1
        
        return curr