# https://leetcode.com/problems/zigzag-conversion

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * min(numRows, len(s))
        currRow, facingDown = 0, False

        for c in s:
            rows[currRow] += c

            if currRow == 0 or currRow == (numRows - 1):
                facingDown = not facingDown
            
            currRow += 1 if facingDown else -1
        
        return ''.join(rows)

