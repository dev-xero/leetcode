# https://leetcode.com/problems/same-tree

"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p or not q or p.val != q.val:
            return False

        qP, qQ = [p], [q] # queues for p and q trees

        while qP and qQ:
            nP = qP.pop(0)
            nQ = qQ.pop(0)

            if nP.val != nQ.val:
                return False

            # check left nodes of both p and q
            if nP.left and nQ.left:
                qP.append(nP.left)
                qQ.append(nQ.left)
            
            elif nP.left or nQ.left:
                return False # one has a child while the other doesn't
            
            # check right nodes of both p and q
            if nP.right and nQ.right:
                qP.append(nP.right)
                qQ.append(nQ.right)

            elif nP.right or nQ.right:
                return False # same, either one has a child but not both
        
        return len(qP) == len(qQ)