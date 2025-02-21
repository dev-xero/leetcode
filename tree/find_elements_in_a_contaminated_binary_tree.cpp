// https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree

#include <bits/stdc++.h>
#include <queue>

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
class FindElements {
    /**
     * Given a binary tree with the following rules:
     * 
     * - root.val == 0
     * - For any treeNode:
     *  - If treeNode.val has a value x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
     *  - If treeNode.val has a value x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
     * 
     * Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.
     * 
     * Implement the FindElements class:
     * 
     * - FindElements(TreeNode* root) Initializes the object with a contaminated 
     *   binary tree and recovers it.
     * - bool find(int target) Returns true if the target value exists in the 
     *   recovered binary tree.
     */
public:
    unordered_set<int> values = {0};

    FindElements(TreeNode* root) {
        queue<TreeNode*> tque;

        root->val = 0;
        tque.push(root);

        while (!tque.empty()) {
            TreeNode* curr = tque.front();
            tque.pop();

            if (curr->left) {
                int leftVal = 2 * curr->val + 1;
                curr->left->val = leftVal;

                tque.push(curr->left);
                values.insert(leftVal);
            }

            if (curr->right) {
                int rightVal = 2 * curr->val + 2;
                curr->right->val = rightVal;

                tque.push(curr->right);
                values.insert(rightVal);
            }
        }
    }

    bool find(int target) { return values.find(target) != values.end(); }
};

/**
 * Your FindElements object will be instantiated and called as such:
 * FindElements* obj = new FindElements(root);
 * bool param_1 = obj->find(target);
 */