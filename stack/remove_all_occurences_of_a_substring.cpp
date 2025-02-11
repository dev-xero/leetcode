// https://leetcode.com/problems/remove-all-occurrences-of-a-substring

#include <string>

class Solution {
public:
    std::string removeOccurrences(std::string s, std::string part) {
        /**
         * Given two strings s and part, perform the following operation on
         * s until all occurrences of the substring part are removed:
         *  Find the leftmost occurrence of the substring part and remove it from s.
         * Return s after removing all occurrences of part. 
         * 
         * A substring is a contiguous sequence of characters in a string.
         */
        std::string result;
        int M = part.size();
        char endPart = part.back();

        for (char ch : s) {
            result.push_back(ch);
            
            if (ch == endPart && result.size() >= M) {
                if (result.substr(result.size() - M) == part) {
                    result.erase(result.size() - M);
                }
            }
        }

        return result;
    }
};