#include <string>

class Solution {
public:
    std::string clearDigits(std::string s) {
        /**
         * You are given a string s. Your task is to remove all digits 
         * by doing this operation repeatedly: 
         * Delete the first digit and the closest non-digit character 
         * to its left.
         * 
         * Return the resulting string after removing all digits.
         */
        std::string stack;

        for (auto ch : s) {
            if (isdigit(ch)) {
                if (!stack.empty()) {
                    stack.pop_back();
                }
            } else {
                stack.push_back(ch);
            }
        }

        return stack;
    }
};