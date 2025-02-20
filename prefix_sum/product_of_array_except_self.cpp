// https://leetcode.com/problems/product-of-array-except-self

#include <vector>

using namespace std;

class Solution {
    /**
     * Given an integer array nums, return an array answer such that answer[i] is equal 
     * to the product of all the elements of nums except nums[i].
     * 
     * The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
     * 
     * You must write an algorithm that runs in O(n) time and without using the division operation.
     */
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int N = nums.size();
        
        vector<int> prefix(N);
        vector<int> suffix(N);
        vector<int> ret(N);

        prefix[0] = nums[0];
        suffix[N-1] = nums[N-1];

        for (int i = 1; i < N; i++)
            prefix[i] = prefix[i-1] * nums[i];

        for (int j = N - 2; j > -1; j--)
            suffix[j] = suffix[j+1] * nums[j];

        for (int idx = 0; idx < N; idx++) {
            if (idx == 0) ret[0] = suffix[1];
            else if (idx == N-1) ret[N-1] = prefix[N-2];
            else ret[idx] = prefix[idx-1] * suffix[idx+1];
        }

        return ret;
    }
};