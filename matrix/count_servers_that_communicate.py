# https://leetcode.com/problems/count-servers-that-communicate

"""
You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.
"""


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        row_count = [0] * m
        col_count = [0] * n

        for row in range(m):
            for col in range(n):
                if grid[row][col]:
                    row_count[row] += 1
                    col_count[col] += 1

        count = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] and (row_count[row] > 1 or col_count[col] > 1):
                    count += 1

        return count
