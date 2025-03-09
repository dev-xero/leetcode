// https://leetcode.com/problems/alternating-groups-i

#include <bits/stdc++.h>

using namespace std;

class Solution {
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