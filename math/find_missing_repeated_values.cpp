// https://leetcode.com/problems/find-missing-and-repeated-values

#include <bits/stdc++>

using namespace std;

class Solution {
  /**
   *
   * You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. 
   * Each integer appears exactly once except a which appears twice and b which is missing. The task 
   * is to find the repeating and missing numbers a and b.
   *
   * Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.
   */
public:
    vector<int> findMissingAndRepeatedValues(vector<vector<int>>& grid) {
        unordered_set<int> seen;
        int N = grid[0].size();
        
        int repeating = 0;
        int gridSum = 0;

        for (int i = 0; i < N; i++) {            
            for (int j = 0; j < N; j++) {
                int num = grid[i][j];
                gridSum += num;

                if (seen.count(num) > 0) {
                    repeating = num;
                    gridSum -= num;
                }

                seen.insert(num);
            }
        }

        int gaussSum = (N*N) * 0.5 * (N*N + 1);

        return {repeating, gaussSum - gridSum};
    }
};
