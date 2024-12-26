# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree

"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a
height-balanced binary search tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def buildTree(arr):
            if not arr:
                return None
            
            mid = len(arr) // 2
            node = TreeNode(arr[mid])
            
            node.left = buildTree(arr[:mid])
            node.right = buildTree(arr[mid+1:])

            return node

        return buildTree(nums)
