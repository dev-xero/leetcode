// https://leetcode.com/problems/number-of-substrings-containing-all-three-characters

#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  /**
   * Given a string s consisting only of characters a, b and c.
   *
   * Return the number of substrings containing at least one 
   * occurrence of all these characters a, b and c.
   */
    int numberOfSubstrings(string s) {
        int N = s.length();
        int res = 0;
        int left = 0, right = 0;
        
        int freq[3] = { 0 };

        while (right < N) {
            freq[s[right] - 'a']++;
            while (hasAllChars(freq)) {
                res += N - right;
                freq[s[left] - 'a']--;
                left++;
            }
            right++;
        }

        return res;
    }

private:
    bool hasAllChars(int *freq) {
        return freq[0] > 0 && freq[1] > 0 && freq[2] > 0;
    }
};
