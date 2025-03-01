// https://leetcode.com/problems/apply-operations-to-an-array

#include <vector>

using namespace std;

class Solution {
   public:
    vector<int> applyOperations(vector<int>& nums) {
        int N = nums.size();

        // merge pass
        for (int i = 1; i < N; i++) {
            if (nums[i] == nums[i - 1]) {
                nums[i - 1] *= 2;
                nums[i] = 0;
            }
        }

        // swap pass
        int write = 0;
        for (int read = 0; read < N; read++) {
            if (nums[read] != 0) {
                swap(nums[read], nums[write]);
                write++;
            }
        }

        return nums;
    }
};