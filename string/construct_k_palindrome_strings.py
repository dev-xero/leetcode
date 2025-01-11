# https://leetcode.com/problems/construct-k-palindrome-strings

"""
Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.
"""

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        
        oddCounts = 0
        seenChars = set()

        for char in s:
            if not char in seenChars:
                thisCharCount = s.count(char)
                
                if thisCharCount % 2 == 1:
                    oddCounts += 1
                
                seenChars.add(char)

        return oddCounts <= k
