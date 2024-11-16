# https://leetcode.com/problems/longest-substring-without-repeating-characters

"""
Given a string s, find the length of the longest
substring
without repeating characters.

Example 1:
    - Input: s = "abcabcbb"
    - Output: 3
    - Explanation: The answer is "abc", with the length of 3.

Example 2:
    - Input: s = "bbbbb"
    - Output: 1
    - Explanation: The answer is "b", with the length of 1.

Example 3:
    - Input: s = "pwwkew"
    - Output: 3
    - Explanation: The answer is "wke", with the length of 3. Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Essentially, the use the sliding window technique to satisfy uniqueness
        constraint.

        We initialize two pointers: left = 0 and right = 1, then track the max
        length and characters seen so far.

        If the right pointer isn't on a character we have already seen, we keep
        incrementing the pointer and updating our seen set.

        If we are however, on a character we've seen before, we keep shrinking the
        window by incrementing the left pointer and removing seen until we are not.

        Max seen length is computed on each outer iteration by:
            formula = right_pointer - left_pointer + 1
        """

        size = len(s)

        if size <= 1:
            return size

        lp = 0
        rp = 1

        seen = set(s[0])
        max_seen = 0

        while rp < size:
            while s[rp] in seen:
                seen.remove(s[lp])
                lp += 1
            
            seen.add(s[rp])
            max_seen = max(max_seen, rp - lp + 1)
            rp += 1
        
        return max_seen