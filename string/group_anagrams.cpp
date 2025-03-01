// https://leetcode.com/problems/group-anagrams

#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
    /**
     * Given an array of strings strs, group the together. You can return the answer in any order.
     */
   public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> anagrams;
        unordered_map<string, vector<string>> groups;

        for (string str : strs) {
            // count frequencies
            int freq[26] = {};
            for (char ch : str) {
                freq[ch - 'a'] += 1;
            }

            // frequency-pattern
            string pattern;
            for (int f : freq) {
                pattern += to_string(f) + '#';
            }

            groups[pattern].push_back(str);
        }

        for (auto& entry : groups) {
            anagrams.push_back(entry.second);
        }

        return anagrams;
    }
};