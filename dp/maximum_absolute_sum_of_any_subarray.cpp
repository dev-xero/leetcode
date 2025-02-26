// https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray

#include <vector>

using namespace std;

class Solution {
    /**
     * You are given an integer array nums. The absolute sum of a subarray 
     * [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).
     * 
     * Return the maximum absolute sum of any (possibly empty) subarray of nums.
     * 
     * Note that abs(x) is defined as follows:
     * 
     * If x is a negative integer, then abs(x) = -x.
     * If x is a non-negative integer, then abs(x) = x.
     */
   public:
    int maxAbsoluteSum(vector<int>& nums) {
        int prefix = 0, minSum = 0, maxSum = 0;

        for (int i = 0; i < nums.size(); i++) {
            prefix += nums[i];

            if (prefix < minSum) minSum = prefix;
            if (prefix > maxSum) maxSum = prefix;
        }

        return maxSum - minSum;
    }
};