// https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum

#include <vector>

using namespace std;

class Solution {
    /**
     * Given an array of integers arr, return the number of subarrays with an odd sum.
     * Since the answer can be very large, return it modulo 109 + 7.
     */
   public:
    int numOfSubarrays(vector<int>& arr) {
        int N = arr.size();
        const int MOD = 1e9 + 7;

        int prefixSum = 0;
        int count = 0;
        int oddCount = 0, evenCount = 1;

        for (int num : arr) {
            prefixSum += num;
            if (prefixSum % 2 == 0) {
                count += oddCount;
                evenCount++;
            } else {
                count += evenCount;
                oddCount++;
            }

            count %= MOD;
        }

        return count;
    }
};