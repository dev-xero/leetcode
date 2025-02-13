// https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii

#include <queue>
#include <vector>
#include <functional>

class Solution {
public:
    int minOperations(std::vector<int>& nums, int k) {
        /**
         *  You are given a 0-indexed integer array nums, and an integer k.
         * In one operation, you will:
         *      Take the two smallest integers x and y in nums.
         *      Remove x and y from nums.
         *      Add min(x, y) * 2 + max(x, y) anywhere in the array.
         * 
         * Note that you can only apply the described operation if nums contains 
         * at least two elements.
         * 
         * Return the minimum number of operations needed so that all elements of 
         * the array are greater than or equal to k.
         */
        std::priority_queue<long, std::vector<long>, std::greater<long>> min_heap(nums.begin(), nums.end());
        int ops = 0;

        while (min_heap.top() < k) {
            long x = min_heap.top();
            min_heap.pop();

            long y = min_heap.top();
            min_heap.pop();

            long z = std::min(x, y) * 2 + std::max(x, y);
            min_heap.push(z);

            ops++;
        }

        return ops;
    }
};