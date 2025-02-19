// https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n

#include <string>
#include <vector>

using namespace std;

class Solution {
/**
 * A happy string is a string that:
 *  - consists only of letters of the set ['a', 'b', 'c'].
 *  - s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
 * 
 * For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.
 * 
 * Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.
 * Return the kth string of this list or return an empty string if there are less than k happy strings of length n.
 */
public:
    int count = 0;
    string result = "";

    string backtrack(string str, vector<char>& alpha, int i, int n, int k) {
        if (str.size() == n) {
            count += 1;
            if (count == k) {
                result = str;
            }
            return "";
        }

        for (char ch : alpha) {
            if (str.size() > 0 && str.back() == ch) {
                continue;
            }
            str += ch;
            backtrack(str, alpha, i + 1, n, k);
            str.pop_back();
        }

        return "";

    }

    string getHappyString(int n, int k) {
        vector<char> alpha = {'a', 'b', 'c'};
        backtrack("", alpha, 1, n, k);
        return result;
    }
};