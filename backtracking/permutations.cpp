// https://leetcode.com/problems/permutations

#include <vector>

using namespace std;

class Solution {
    /**
     * Given an array nums of distinct integers, return all the possible permutations. 
     * 
     * You can return the answer in any order.
     */
public:
    vector<vector<int>>result;
    
    void backtrack(int i, vector<int>& nums, vector<int>& perms, vector<bool> used) {
        if (perms.size() == nums.size()) {
            result.push_back(perms);
            return;
        }

        for (int i = 0; i < nums.size(); i++) {
            if (!used[i]) {
                used[i] = true;
                perms.push_back(nums[i]);

                backtrack(i+1, nums, perms, used);

                perms.pop_back();
                used[i] = false;
            }
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {
        vector<bool> used(nums.size(), false);
        vector<int> perms;

        backtrack(0, nums, perms, used);

        return result;
    }
};