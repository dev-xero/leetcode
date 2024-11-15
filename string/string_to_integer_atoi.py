# https://leetcode.com/problems/string-to-integer-atoi

"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

- Whitespace: Ignore any leading whitespace (" ").

- Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.

- Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.

- Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.

Return the integer as the final result.
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        
        sign = 1
        
        if s[0] == '-' or s[0] == '+':
            sign = -1 if s[0] == '-' else 1
            s = s[1:]
        
        idx = 0
        result = 0

        MIN = -2**31
        MAX = 2**31 - 1
        
        while idx < len(s) and s[idx].isdigit():
            digit = int(s[idx])

            if result > MAX // 10 or result == MAX // 10 and digit > (7 if sign == 1 else 8):
                return MAX if sign == 1 else MIN
            
            result = result*10 + digit
            idx += 1
        
        # if not read:
        #     return 0
        
        return sign * result
