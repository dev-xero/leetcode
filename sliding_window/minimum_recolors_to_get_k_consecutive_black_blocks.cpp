// https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks

#include <bits/stdc++.h>

using namespace std;

class Solution {
    /**
     * You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', 
     * representing the color of the ith block. The characters 'W' and 'B' denote the colors white 
     * and black, respectively.
     * 
     * You are also given an integer k, which is the desired number of consecutive black blocks.
     * 
     * In one operation, you can recolor a white block such that it becomes a black block.
     * 
     * Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.
     */
   public:
    int minimumRecolors(string blocks, int k) {
        int numWhites = 0, left = 0;
        int minRecolors = INT_MAX;

        for (int right = 0; right < blocks.length(); right++) {
            if (blocks[right] == 'W') numWhites++;

            if (right - left + 1 == k) {
                minRecolors = min(minRecolors, numWhites);

                if (blocks[left] == 'W') numWhites--;

                left++;
            }
        }

        return minRecolors;
    }
};