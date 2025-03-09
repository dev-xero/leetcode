// https://leetcode.com/problems/alternating-groups-i

#include <bits/stdc++.h>

using namespace std;

class Solution {
    /**
     * There is a circle of red and blue tiles. You are given an array of
     integers colors.
     * The color of tile i is represented by colors[i]:
     *
     * colors[i] == 0 means that tile i is red.
     * colors[i] == 1 means that tile i is blue.
     *
     Every 3 contiguous tiles in the circle with alternating colors (the middle
     tile has a different color from its left and right tiles) is called an
     alternating group.

     Return the number of alternating groups.

     Note that since colors represents a circle, the first and the last tiles
     are considered to be next to each other.
     */
   public:
    int numberOfAlternatingGroups(vector<int>& colors) {
        int groups = 0;
        int N = colors.size();

        for (int i = 0; i < N; i++) {
            int prev = 0;
            int next = 0;

            if (i == 0) {
                prev = colors[N - 1];
                next = colors[i + 1];
            } else if (i == N - 1) {
                prev = colors[i - 1];
                next = colors[0];
            } else {
                next = colors[i + 1];
                prev = colors[i - 1];
            }

            if (prev == next && prev != colors[i]) {
                groups++;
            }
        }

        return groups;
    }
};