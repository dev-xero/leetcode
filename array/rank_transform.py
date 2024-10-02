# https://leetcode.com/problems/rank-transform-of-an-array

"""
Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.
"""


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sarr = sorted(list(set(arr)))
        numrank = {}

        for idx in range(len(sarr)):
            numrank[sarr[idx]] = idx + 1

        for idx in range(len(arr)):
            arr[idx] = numrank[arr[idx]]

        return arr
