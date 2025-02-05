# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        """
            You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

            Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.
        """
        if s1 == s2:
            return True

        N = len(s1)
        
        s1_map = [0] * 26
        s2_map = [0] * 26
        
        diff = 0

        for i in range(N):
            s1_char, s2_char = s1[i], s2[i]
            if s1_char != s2_char:
                diff += 1

            if diff > 2:
                return False

            s1_map[ord(s1_char) - ord('a')] += 1
            s2_map[ord(s2_char) - ord('a')] += 1
        

        return s1_map == s2_map