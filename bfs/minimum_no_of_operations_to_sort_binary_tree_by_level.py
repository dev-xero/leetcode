# https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level

"""
You are given the root of a binary tree with unique values.

In one operation, you can choose any two nodes at the same level and swap their values.

Return the minimum number of operations needed to make the values at each level sorted in a strictly increasing order.

The level of a node is the number of edges along the path between it and the root node.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # we use bfs and cycle sort
    def minSwaps(self, original: list) -> int:
        swaps = 0
        target = sorted(original)

        pos = { val: idx for idx, val in enumerate(original) }

        for i in range(len(original)):
            if original[i] != target[i]:
                swaps += 1
                # update position
                cur = pos[target[i]] # index
                pos[original[i]] = cur
                original[cur] = original[i]

        return swaps

    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        que = [root]
        swaps = 0

        while que:
            size = len(que)
            vals = []

            # cache level values and add children to queue
            for _ in range(size):
                node = que.pop(0)
                vals.append(node.val)

                if node.left:
                    que.append(node.left)
                
                if node.right:
                    que.append(node.right)

            # compute minimum swaps
            swaps += self.minSwaps(vals)

        return swaps
