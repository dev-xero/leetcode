// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal

#include <vector>

using namespace std;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
class Solution {
    /**
     * Given two integer arrays, preorder and postorder where preorder is the preorder 
     * traversal of a binary tree of distinct values and postorder is the postorder 
     * traversal of the same tree, reconstruct and return the binary tree.
     * 
     * If there exist multiple answers, you can return any of them.
     */
   private:
    TreeNode* constructTree(int preStart, int preEnd, int postStart,
                            vector<int>& preorder,
                            vector<int>& indexInPostOrder) {
        if (preStart > preEnd) return NULL;

        if (preStart == preEnd) return new TreeNode(preorder[preStart]);

        int leftRoot = preorder[preStart + 1];
        int numOfNodesInLeft = indexInPostOrder[leftRoot] - postStart + 1;

        TreeNode* root = new TreeNode(preorder[preStart]);
        root->left = constructTree(preStart + 1, preStart + numOfNodesInLeft,
                                   postStart, preorder, indexInPostOrder);
        root->right = constructTree(preStart + numOfNodesInLeft + 1, preEnd,
                                    postStart + numOfNodesInLeft, preorder,
                                    indexInPostOrder);

        return root;
    }

   public:
    TreeNode* constructFromPrePost(vector<int>& preorder,
                                   vector<int>& postorder) {
        int numOfNodes = preorder.size();
        vector<int> indexInPostOrder(numOfNodes + 1);

        for (int index = 0; index < numOfNodes; index++) {
            indexInPostOrder[postorder[index]] = index;
        }

        return constructTree(0, numOfNodes - 1, 0, preorder, indexInPostOrder);
    }
};