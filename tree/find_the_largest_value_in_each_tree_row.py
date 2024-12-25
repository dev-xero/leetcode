# https://leetcode.com/problems/find-largest-value-in-each-tree-row/

"""
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        que, ans = [root], []
        lvl = 1

        while que:
            k = len(que)
            m = -inf
            for _ in range(k):
                node = que.pop(0)
                m = max(m, node.val)

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            ans.append(m)

        return ans
