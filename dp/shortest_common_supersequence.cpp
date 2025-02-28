// https://leetcode.com/problems/shortest-common-supersequence

#include <string>
#include <vector>

using namespace std;

class Solution {
    /**
     * Given two strings str1 and str2, return the shortest string that has both str1 
     * and str2 as subsequences. If there are multiple valid strings, return any of them.
     * 
     * A string s is a subsequence of string t if deleting some number of characters 
     * from t (possibly 0) results in the string s.
     */
   public:
    string shortestCommonSupersequence(string str1, string str2) {
        int m = str1.length();
        int n = str2.length();

        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

        // initialize dp-table for base cases
        for (int row = 0; row <= m; row++) dp[row][0] = row;

        for (int col = 0; col <= n; col++) dp[0][col] = col;

        // scs-fill
        for (int row = 1; row <= m; row++) {
            for (int col = 1; col <= n; col++) {
                if (str1[row - 1] == str2[col - 1]) {
                    dp[row][col] = dp[row - 1][col - 1] + 1;
                } else {
                    dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + 1;
                }
            }
        }

        // backtracking
        string seq = "";
        int row = m, col = n;
        while (row > 0 && col > 0) {
            // both match, move diagonally
            if (str1[row - 1] == str2[col - 1]) {
                seq += str1[row - 1];
                row--;
                col--;
                // row < col, move up
            } else if (dp[row - 1][col] < dp[row][col - 1]) {
                seq += str1[row - 1];
                row--;
                // move left
            } else {
                seq += str2[col - 1];
                col--;
            }
        }

        // fill remaining chars from s1 & s2
        while (row > 0) {
            seq += str1[row - 1];
            row--;
        }
        while (col > 0) {
            seq += str2[col - 1];
            col--;
        }

        reverse(seq.begin(), seq.end());
        return seq;
    }
};