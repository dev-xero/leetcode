// https://leetcode.com/problems/longest-common-subsequence

#include <vector>
#include <string>

using namespace std;

class Solution {
    /**
     * Given two strings text1 and text2, return the length of their longest common subsequence. 
     * If there is no common subsequence, return 0.
     * 
     * A subsequence of a string is a new string generated from the original string with some 
     * characters (can be none) deleted without changing the relative order of the remaining characters.
     * 
     * For example, "ace" is a subsequence of "abcde". A common subsequence of two strings is a 
     * subsequence that is common to both strings.
     */
    private:
        int lcs(string& s1, string& s2, int m, int n, vector<vector<int>>& dp) {
            if (m == 0 || n == 0)
                return 0;
            
            // computed already
            if (dp[m][n] != -1)
                return dp[m][n];
    
            // ends match
            if (s1[m-1] == s2[n-1])
                return dp[m][n] = 1 + lcs(s1, s2, m-1, n-1, dp);
    
            // ends do not match
            return dp[m][n] = max(lcs(s1, s2, m-1, n, dp), lcs(s1, s2, m, n-1, dp));
        }
    public:
        int longestCommonSubsequence(string text1, string text2) {
            // algorithm:
            // we have a 2D-dp array to store the lengths at those indices
            int m = text1.size();
            int n = text2.size();
            vector<vector<int>> dp(m + 1, vector<int>(n + 1, -1));
    
            return lcs(text1, text2, m, n, dp);
        }
    };