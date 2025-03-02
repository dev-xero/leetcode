// https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values

#include <string>
#include <vector>

using namespace std;

class Solution {
    /**
     * You are given two 2D integer arrays nums1 and nums2.
     * nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
     * nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
     * 
     * Each array contains unique ids and is sorted in ascending order by id.
     * 
     * Merge the two arrays into one array that is sorted in ascending order by id, respecting 
     * the following conditions:
     * 
     * Only ids that appear in at least one of the two arrays should be included in the resulting array.
     * Each id should be included only once and its value should be the sum of the values of this id 
     * in the two arrays. If the id does not exist in one of the two arrays, then assume its value in that array to be 0.
     * 
     * Return the resulting array. The returned array must be sorted in ascending order by id.
     */
   public:
    vector<vector<int>> mergeArrays(vector<vector<int>>& nums1,
                                    vector<vector<int>>& nums2) {
        vector<vector<int>> merged;
        int p1 = 0, p2 = 0;
        int L1 = nums1.size(), L2 = nums2.size();

        // Mergesort
        while (p1 < L1 && p2 < L2) {
            int id1 = nums1[p1][0];
            int id2 = nums2[p2][0];

            if (id1 == id2) {
                merged.push_back({id1, nums1[p1][1] + nums2[p2][1]});
                p1++;
                p2++;
            } else if (id1 < id2) {
                merged.push_back(nums1[p1]);
                p1++;
            } else {
                merged.push_back(nums2[p2]);
                p2++;
            }
        }

        // Fill remaining elements from nums1 and nums2
        while (p1 < L1) {
            merged.push_back(nums1[p1]);
            p1++;
        }

        while (p2 < L2) {
            merged.push_back(nums2[p2]);
            p2++;
        }

        return merged;
    }
};