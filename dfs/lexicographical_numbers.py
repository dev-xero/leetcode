# https://leetcode.com/problems/lexicographical-numbers

"""
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space. 
"""


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def dfs(current, limit):
            if current > limit:
                return

            result.append(current)

            for i in range(10):
                if current * 10 + i > limit:
                    break

                dfs(current * 10 + i, limit)

        result = []
        for i in range(1, 10):
            dfs(i, n)

        return result
