#include <vector>

class Solution {
public:
    int maximumSum(std::vector<int>& nums) {
        /**
         * You are given a 0-indexed array nums consisting of positive integers. 
         * You can choose two indices i and j, such that i != j, and the sum of 
         * digits of the number nums[i] is equal to that of nums[j].
         * 
         * Return the maximum value of nums[i] + nums[j] that you can obtain over 
         * all possible indices i and j that satisfy the conditions.
         */
        int max[82] = {0};
        int maxEqSum = -1;

        for (int x : nums) {
            int sum = 0;
            int temp = x;

            while (temp > 0) {
                sum += temp % 10;
                temp /= 10;
            }

            if (max[sum] != 0)
                maxEqSum = std::max(maxEqSum, x + max[sum]);
            
            max[sum] = std::max(max[sum], x);
        }

        return maxEqSum;
    }
};