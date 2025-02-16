// https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence

#include <vector>;

using namespace std;

class Solution {
    /**
     * Given an integer n, find a sequence that satisfies all of the following:
     *  - The integer 1 occurs once in the sequence. 
     *  - Each integer between 2 and n occurs twice in the sequence.
     *  - For every integer i between 2 and n, the distance between the two occurrences of i is exactly i.
     * 
     * The distance between two numbers on the sequence, a[i] and a[j], is the absolute difference of their indices, |j - i|.
     * 
     * Return the lexicographically largest sequence. It is guaranteed that under the given constraints, 
     * there is always a solution.
     * 
     * A sequence a is lexicographically larger than a sequence b (of the same length) if in the first 
     * position where a and b differ, sequence a has a number greater than the corresponding number in b. 
     * For example, [0,1,9,0] is lexicographically larger than [0,1,5,6] because the first position 
     * they differ is at the third number, and 9 is greater than 5.
     * 
     */
public:
    bool backtrack(
        int index,
        int n,
        int size, 
        vector<int>& result, 
        vector<bool>& used
    ) {
        if (index == size) return true;
        if (result[index] != 0) return backtrack(index+1, n, size, result, used);

        for (int num = n; num > 0; num--) {
            if (used[num]) continue;

            if (num == 1) {         
                result[index] = 1;
                used[num] = true;

                if (backtrack(index + 1, n, size, result, used))
                    return true;
                
                result[index] = 0;
                used[num] = false;

            } else {
                int next_index = index + num;
                
                if (next_index < size && result[next_index] == 0) {
                    result[index] = num;
                    result[next_index] = num;
                    used[num] = true;

                    if (backtrack(index + 1, n, size, result, used))
                        return true;
                    
                    result[index] = 0;
                    result[next_index] = 0;
                    used[num] = false;
                }
            }
        }

        return false;
    }

    vector<int> constructDistancedSequence(int n) {
        int size = 2 * n - 1;
        vector<int> result(size, 0);
        vector<bool> used(n + 1, false);

        backtrack(0, n, size, result, used);

        return result;
    }
};