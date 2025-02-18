// https://leetcode.com/problems/construct-smallest-number-from-di-string

#include <vector>
#include <stack>
#include <string>

using namespace std;

class Solution {
public:
    string smallestNumber(string pattern) {
        /**
         * You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning 
         * increasing and 'D' meaning decreasing.
         * 
         * A 0-indexed string num of length n + 1 is created using the following conditions:
         *  - num consists of the digits '1' to '9', where each digit is used at most once.
         *  - If pattern[i] == 'I', then num[i] < num[i + 1].
         *  - If pattern[i] == 'D', then num[i] > num[i + 1].
         *  
         * Return the lexicographically smallest possible string num that meets the conditions.
         */
        string result;
        stack<int> numStack;

        for (int index = 0; index <= pattern.size(); index++) {
            numStack.push(index + 1);
            if (pattern[index] == 'I' || index == pattern.size()) {
                while (!numStack.empty()) {
                    result += to_string(numStack.top());
                    numStack.pop();
                }
            }
        }

        return result;
    }
};