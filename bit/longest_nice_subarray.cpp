// https://leetcode.com/problems/longest-nice-subarray

#include <bits/stdc++.h>

using namespace std;

class Solution {
    /**
     * You are given an array nums consisting of positive integers.
     * We call a subarray of nums nice if the bitwise AND of every pair
     * of elements that are in different positions in the subarray is
     * equal to 0.
     *
     * Return the length of the longest nice subarray.
     * A subarray is a contiguous part of an array.
     * Note that subarrays of length 1 are always considered nice
     */
  public:
    int longestNiceSubarray(vector<int> &nums) {
        int left = 0;
        int right = 0;
        int maxLength = 1;
        int usedBits = 0;
        while (right < nums.size()) {
            while ((nums[right] & usedBits) != 0) {
                usedBits ^= nums[left];
                left++;
            }
            usedBits |= nums[right];
            maxLength = max(maxLength, right - left + 1);
            right++;
        }
        return maxLength;
    }
};
