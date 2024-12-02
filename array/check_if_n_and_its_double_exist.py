# https://leetcode.com/problems/check-if-n-and-its-double-exist

"""
Given an array arr of integers, check if there exist two indices i and j such that :

- i != j
- 0 <= i, j < arr.length
- arr[i] == 2 * arr[j]
"""


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()

        for i in range(len(arr)):
            if (arr[i] * 2) in seen or (arr[i] / 2) in seen:
                return True

            seen.add(arr[i])

        return False
