// https://leetcode.com/problems/merge-strings-alternately

#include <string>
#include <vector>

using namespace std;

class Solution {
    /**
     * You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
     *  starting with word1. If a string is longer than the other, append the additional letters onto the 
     * end of the merged string.
     * 
     * Return the merged string.
     */
   public:
    string mergeAlternately(string word1, string word2) {
        int L1 = word1.length(), L2 = word2.length();
        int p1 = 0, p2 = 0;

        string res = "";

        while (p1 < L1 || p2 < L2) {
            if (p1 < L1) {
                res += word1[p1];
                p1++;
            }
            if (p2 < L2) {
                res += word2[p2];
                p2++;
            }
        }

        return res;
    }
};