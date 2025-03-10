// https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii

#include <bits/stdc++>

using namespace std;

class Solution {
  /**
   * You are given a string word and a non-negative integer k.
   *
   * Return the total number of of word that contain every 
   * vowel ('a', 'e', 'i', 'o', and 'u') at least once and 
   * exactly k consonants.
   */
public:
    long long countOfSubstrings(string word, int k) {
        return atLeastK(word, k) - atLeastK(word, k+1);
    }

private:
    long atLeastK(string word, int k) {
        long matches = 0;
        int left = 0, right = 0;
        
        unordered_map<char, int> vowels;
        int consonants = 0;

        // start sliding window
        while (right < word.length()) {
            char newLetter = word[right];

            if (isVowel(newLetter))
                vowels[newLetter]++;
            else
                consonants++;
            
            // update our window
            while (vowels.size() == 5 and consonants >= k) {
                matches += word.length() - right;
                char startLetter = word[left];

                if (isVowel(startLetter)) {
                    if (--vowels[startLetter] == 0) {
                        vowels.erase(startLetter);
                    }
                } else {
                    consonants--;
                }
                left++;
            }

            right++;
        }
        
        return matches;
    }

    bool isVowel(char ch) {
        return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u';
    }
};
