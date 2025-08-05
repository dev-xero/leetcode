// https://leetcode.com/problems/fruits-into-baskets-ii

#include <vector>

using namespace std;

class Solution {
  public:
    int numOfUnplacedFruits(vector<int> &fruits, vector<int> &baskets) {
        // ==========================================================
        // Intuition
        // ----------------------------------------------------------
        // Brute force nested loops come to mind
        // ==========================================================
        int n = fruits.size();
        int count = 0;
        for (int fruit : fruits) {
            int unplaced = 1;
            for (int j = 0; j < n; j++) {
                if (fruit <= baskets[j]) {
                    baskets[j] = 0;
                    unplaced = 0;
                    break;
                }
            }
            count += unplaced;
        }
        return count;
    }
};
