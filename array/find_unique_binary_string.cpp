// https://leetcode.com/problems/find-unique-binary-string

#include <string>
#include <vector>

using namespace std;

class Solution {
    /**
     * Given an array of strings nums containing n unique binary strings each of length n, 
     * return a binary string of length n that does not appear in nums. If there are multiple 
     * answers, you may return any of them.
     */
public:
    string findDifferentBinaryString(vector<string>& nums) {
        string bstring;

        // Interesting application of Cantor's diagonal proof, we could
        // also solve recursively with backtracking. 
        // https://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument
        for (int i = 0; i < nums.size(); i++) {
            char curr = nums[i][i];
            bstring += curr == '0' ? '1' : '0';
        }
        
        return bstring;
    }
};