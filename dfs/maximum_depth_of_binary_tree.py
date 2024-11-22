# https://leetcode.com/problems/maximum-depth-of-binary-tree

"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(depth, node):
            if not node:
                return depth

            d1 = dfs(depth+1, node.left)
            d2 = dfs(depth+1, node.right)

            return max(d1, d2)

        return dfs(0, root)
