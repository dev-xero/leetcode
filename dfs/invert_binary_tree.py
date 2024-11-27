# https://leetcode.com/problems/invert-binary-tree

"""
Given the root of a binary tree, invert the tree, and return its root.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        def invertDFS(curr):
            if curr is None:
                return curr

            right = invertDFS(curr.left)
            left = invertDFS(curr.right)

            if right is not None:
                curr.right = right

            else:
                curr.right = None

            if left is not None:
                curr.left = left

            else:
                curr.left = None

            return curr

        return invertDFS(root)
