# https://leetcode.com/problems/unique-length-3-palindromic-subsequences

"""
Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

- For example, "ace" is a subsequence of "abcde"
"""

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        fo_map = {} # first occurence index map
        lo_map = {} # last occurence index map

        # build a map of the first and last occurences 
        # of each character
        for idx, char in enumerate(s):
            if not char in fo_map:
                fo_map[char] = idx
            
            lo_map[char] = idx
        
        cnt = 0

        for char in fo_map:
            fidx = fo_map[char]
            lidx = lo_map[char]

            # has at least 2 chars between them
            if lidx - fidx >= 2:
                unique = set(s[fidx+1:lidx])
                cnt += len(unique)

        return cnt
    