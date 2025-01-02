# https://leetcode.com/problems/count-vowel-strings-in-ranges

"""
You are given a 0-indexed array of strings words and a 2D array of integers queries.

Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.

Return an array ans of size queries.length, where ans[i] is the answer to the ith query.

Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.
"""

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a', 'e', 'i', 'o', 'u']
        n = len(words)
        pf = [0] * n
        sol = []

        # initialize pf array
        pf[0] = 1 if (words[0][0] in vowels and words[0][-1] in vowels) else 0
        
        # compute prefix sums
        for i in range(1, n):
            if words[i][0] in vowels and words[i][-1] in vowels:
                pf[i] = pf[i-1] + 1
            else:
                pf[i] = pf[i-1]
            
        # check range queries
        for (l, r) in queries:
            if l == 0:
                sol.append(pf[r])
            else:
                sol.append(pf[r] - pf[l-1])

        return sol