// https://leetcode.com/problems/combination-sum

#include <bits/stdc++.h>

using namespace std;

class Solution {
private:
    vector<vector<int>>backtrack(
        vector<int>& candidates, int target, int sum, int i, 
        vector<vector<int>>& result,vector<int>& current
    ) {
        if (sum == target) {
            result.push_back(current);
        } else if (sum < target) {
            for (int j = i; j < candidates.size(); j++) {
                current.push_back(candidates[j]);
                backtrack(candidates, target, sum + candidates[j], j, result, current);
                current.pop_back();
            }
        }

        return result;
    }
    
public:
    /**
     * Given an array of distinct integers candidates and a target integer target,
     * return a list of all unique combinations of candidates where the chosen 
     * numbers sum to target. You may return the combinations in any order.
     *
     * The same number may be chosen from candidates an unlimited number of times.
     * Two combinations are unique if the of at least one of the chosen numbersis
     * is different.
     *
     * The test cases are generated such that the number of unique combinations 
     * that sum up to target is less than 150 combinations for the given input.
     */
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        vector<int> current;

        backtrack(candidates, target, 0, 0, result, current);
        return result;
    }
};
