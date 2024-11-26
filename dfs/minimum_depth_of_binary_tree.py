# https://leetcode.com/problems/minimum-depth-of-binary-tree

"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(depth, node):
            if node is None:
                return depth

            if not node.left:
                return dfs(depth+1, node.right)

            elif not node.right:
                return dfs(depth+1, node.left)

            else:
                dL = dfs(depth+1, node.left)
                dR = dfs(depth+1, node.right)

                return min(dL, dR)

        return dfs(0, root)
