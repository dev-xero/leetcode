// https://leetcode.com/problems/find-the-punishment-number-of-an-integer

using namespace std;

class Solution {
/**
 * Given a positive integer n, return the punishment number of n. The punishment number
 * of n is defined as the sum of the squares of all integers i such that:
 *    - 1 <= i <= n
 *    - The decimal representation of i * i can be partitioned into contiguous substrings 
 *      such that the sum of the integer values of these substrings equals i.
 */
public:
    bool canPartition(int num, int target) {
        if (target < 0 || num < target) {
            return false;
        }

        if (num == target) {
            return true;
        }

        return canPartition(num / 10, target - num % 10) 
            || canPartition(num / 100, target - num % 100) 
            || canPartition(num / 1000, target - num % 1000);
    }

    int punishmentNumber(int n) {
        int punishmentNumber = 0;

        for (int i = 1; i < n + 1; i++) {
            int squared = i * i;

            if (canPartition(squared, i)) {
                punishmentNumber += squared;
            }
        }
        
        return punishmentNumber;
    }
};