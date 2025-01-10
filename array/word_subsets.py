# https://leetcode.com/problems/word-subsets

"""
You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

- For example, "wrr" is a subset of "warrior" but is not a subset of "world".

A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.
"""

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        maxCount = [0] * 26

        # Build max count map
        for word in words2:
            count = [ 0 for k in range(26) ]

            for ch in word:
                idx = ord(ch) - ord('a')
                count[idx] = count[idx] + 1
            
            for i in range(26):
                maxCount[i] = max(maxCount[i], count[i])

        universalWords = []

        # Compare each word in word1 to maxCount
        for word in words1:
            count = [ 0 for k in range(26) ]

            for ch in word:
                idx = ord(ch) - ord('a')
                count[idx] = count[idx] + 1
            
            isUniversal = True

            for i in range(26):
                if count[i] < maxCount[i]:
                    isUniversal = False
                    break
            
            if isUniversal:
                universalWords.append(word)
        
        return universalWords
