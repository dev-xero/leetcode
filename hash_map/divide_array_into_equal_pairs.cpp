#include <bits/stdc++.h>

using namespace std;

class Solution {
    /**
     * You are given an integer array nums consisting of
     * 2 * n integers.
     *
     * You need to divide nums into n pairs such that:
     * - Each element belongs to exactly one pair.
     * -The elements present in a pair are equal.
     *
     *  Return true if nums can be divided into n pairs,
     *  otherwise return false.
     */
  public:
    bool divideArray(vector<int> &nums) {
        unordered_map<int, int> freq;
        for (int num : nums) {
            freq[num]++;
        }
        for (auto pair : freq) {
            if (pair.second % 2) {
                return false;
            }
        }
        return true;
    }
};
