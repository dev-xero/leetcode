"""
You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, m * n].

Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].

Return the smallest index i at which either a row or a column will be completely painted in mat.
"""

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        A = len(arr)
        
        m, n = len(mat[0]), len(mat)
        
        row_freq = [0] * n
        col_freq = [0] * m
        posMap = [0] * (A+1)

        for i in range(n):
            for j in range(m):
                posMap[mat[i][j]] = (i, j)

        for k in range(len(arr)):
            row, col = posMap[arr[k]]

            row_freq[row] += 1
            col_freq[col] += 1
            
            if row_freq[row] == m or col_freq[col] == n:
                return k

        
        return 0
