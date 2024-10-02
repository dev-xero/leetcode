# https://leetcode.com/problems/path-sum

"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        global found
        found = False

        def dfs(root, depth_sum):
            if not root:
                return False

            depth_sum += root.val

            if not root.left and not root.right and depth_sum == targetSum:
                global found
                found = True
                return

            dfs(root.left, depth_sum)
            dfs(root.right, depth_sum)

        dfs(root, 0)
        return found
