# https://leetcode.com/problems/binary-tree-paths

"""
Given the root of a binary tree, return all root-to-leaf paths in any order.
A leaf is a node with no children.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        
        def dfs(curr, path):
            if not curr:
                return None
            
            if path == "":
                path = f"{curr.val}"
            
            else:
                path += f"->{curr.val}"

            if not curr.left and not curr.right:
                paths.append(path)
                return


            dfs(curr.left, path)
            dfs(curr.right, path)
        
        dfs(root, "")

        return paths