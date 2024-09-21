# https://leetcode.com/problems/set-matrix-zeroes

"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        flat_mat = [matrix[i][j] for i in range(rows) for j in range(cols)]
        zero_indices = [i for i, x in enumerate(flat_mat) if x == 0]
        mods = []

        # all rows and cols containing this element must be zero
        for idx in zero_indices:
            which_row = idx // cols
            which_col = idx % cols

            # print("all zeros on row:", which_row)
            # print("all zeros on col:", which_col)
            mods.append([which_row, which_col])
        
        for mod in mods:
            # all rows
            for i in range(0, cols):
                matrix[mod[0]][i] = 0
            
            # all cols
            for i in range(0, rows):
                matrix[i][mod[1]] = 0