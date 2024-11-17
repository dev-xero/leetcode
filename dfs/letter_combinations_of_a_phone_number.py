# https://leetcode.com/problems/letter-combinations-of-a-phone-number

"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        keyboard = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        result = []

        def dfs(depth, limit, seq):
            if depth >= limit:
                result.append(seq)
                return

            for ch in keyboard[digits[depth]]:
                new_sq = seq + ch
                dfs(depth+1, limit, new_sq)

        dfs(0, len(digits), "")

        return result
