# https://leetcode.com/problems/pascals-triangle

"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown.
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = []

        for i in range(numRows):
            row = [1]

            if i > 0:
                prev_row = tri[i-1]
                for j in range(1, i):
                    row.append(prev_row[j-1] + prev_row[j])

            # if not the first row, append 1
            if i > 0:
                row.append(1)

            tri.append(row)

        return tri
