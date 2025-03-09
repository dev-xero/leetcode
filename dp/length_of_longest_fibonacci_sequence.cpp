// https://leetcode.com/problems/length-of-longest-fibonacci-subsequence

#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
    /**
     * A sequence x1, x2, ..., xn is Fibonacci-like if:
     * n >= 3
     * xi + xi+1 == xi+2 for all i + 2 <= n
     * 
     * Given a strictly increasing array arr of positive integers forming a sequence,
     * return the length of the longest Fibonacci-like subsequence of arr. 
     * If one does not exist, return 0.
     * 
     * A subsequence is derived from another sequence arr by deleting any number of 
     * elements (including none) from arr, without changing the order of the remaining
     * elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8]
     */
   public:
    int lenLongestFibSubseq(vector<int>& arr) {
        int N = arr.size();
        int maxlen = 0;

        vector<vector<int>> dp(N, vector<int>(N, 0));
        unordered_map<int, int> valToIndex(N);

        for (int curr = 0; curr < N; curr++) {
            valToIndex[arr[curr]] = curr;

            for (int prev = 0; prev < curr; prev++) {
                int diff = arr[curr] - arr[prev];
                int prevIndex = valToIndex.find(diff) != valToIndex.end()
                                    ? valToIndex[diff]
                                    : -1;

                if (diff < arr[prev] && prevIndex >= 0)
                    dp[prev][curr] = dp[prevIndex][prev] + 1;
                else
                    dp[prev][curr] = 2;

                maxlen = max(maxlen, dp[prev][curr]);
            }
        }

        return maxlen > 2 ? maxlen : 0;
    }
};
