# https://leetcode.com/problems/longest-palindromic-substring

"""
Given a string s, return the longest palindromic substring in s.

A substring is a contiguous non-empty sequence of characters within a string.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        max_len = 1
        max_str = s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))] # dp table

        for i in range(len(s)):
            dp[i][i] = True

            for j in range(i):
                if s[j] == s[i] and (i-j <= 2 or dp[j+1][i-1]):
                    dp[j][i] = True
                    curr = i-j+1

                    if curr > max_len:
                        max_len = curr
                        max_str = s[j:i+1]
        
        return max_str
