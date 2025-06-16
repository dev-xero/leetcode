// https://leetcode.com/problems/maximum-difference-between-increasing-elements

#include <vector>

using namespace std;

class Solution {
    /**
     * Given a 0-indexed integer array nums of size n, find the maximum
     * difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]),
     * such that 0 <= i < j < n and nums[i] < nums[j].
     *
     * Return the maximum difference. If no such i and j exists,
     * return -1.
     */
  public:
    int maximumDifference(vector<int> &nums) {
        int N = nums.size();
        int maxDiff = -1;
        int min = nums[0];
        for (auto j = 1; j < N; j++) {
            if (nums[j] > min) {
                maxDiff = std::max(maxDiff, nums[j] - min);
            } else {
                min = nums[j];
            }
        }
        return maxDiff;
    }
};
