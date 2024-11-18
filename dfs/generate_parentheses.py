# https://leetcode.com/problems/generate-parentheses

"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(op, cl, pattern):
            if op == cl and op + cl == n*2:
                res.append(pattern)
                return

            if op < n:
                dfs(op + 1, cl, pattern + "(")
            
            if cl < op:
                # no. of closing parentheses must be same with open
                dfs(op, cl + 1, pattern + ")")

        dfs(0, 0, "")
        return res
